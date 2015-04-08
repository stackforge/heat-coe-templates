# Copyright 2015 Rackspace inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
import os

from oslo_config import cfg

from magnum.conductor import template_definition as tdef

template_def_opts = [
    cfg.StrOpt('k8s_atomic_template_path',
               default=os.path.join(os.path.dirname(__file__),
                                    'kubecluster.yaml'),
               deprecated_name='template_path',
               deprecated_group='k8s_heat',
               help='Location of template to build a k8s cluster on atomic. '),
]

cfg.CONF.register_opts(template_def_opts, group='bay')


class AtomicK8sTemplateDefinition(tdef.BaseTemplateDefinition):
    provides = [
        {'platform': 'vm', 'os': 'fedora-atomic', 'coe': 'kubernetes'},
    ]

    def __init__(self):
        super(AtomicK8sTemplateDefinition, self).__init__()
        self.add_parameter('external_network_id',
                           baymodel_attr='external_network_id',
                           required=True)

        self.add_parameter('dns_nameserver',
                           baymodel_attr='dns_nameserver')
        self.add_parameter('master_flavor',
                           baymodel_attr='master_flavor_id')
        self.add_parameter('fixed_network',
                           baymodel_attr='fixed_network')
        self.add_parameter('number_of_minions',
                           bay_attr='node_count',
                           param_type=str)
        self.add_parameter('docker_volume_size',
                           baymodel_attr='docker_volume_size')
        # TODO(yuanying): Add below lines if apiserver_port parameter
        # is supported
        # self.add_parameter('apiserver_port',
        #                    baymodel_attr='apiserver_port')

        self.add_output('kube_master',
                        bay_attr='api_address')
        self.add_output('kube_minions_external',
                        bay_attr='node_addresses')

    def template_path(self):
        return cfg.CONF.bay.k8s_atomic_template_path2
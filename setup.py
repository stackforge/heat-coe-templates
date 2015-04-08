#!/usr/bin/env python
# Copyright (c) 2015 Rackspace Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import setuptools

setuptools.setup(
    name="HeatCOETemplates",
    version="0.0.1",
    packages=['heat_coe_templates'],
    include_package_data=True,
    install_requires=['magnum', 'oslo.config'],
    author="OpenStack",
    author_email="openstack-dev@lists.openstack.org",
    description="Default COE Templates for Magnum",
    license="Apache",
    keywords="magnum templates",
    entry_points={
        'magnum.template_definitions': [
            'vm_atomic_k8s = heat_coe_templates:AtomicK8sTemplateDefinition',
        ]
    }
)

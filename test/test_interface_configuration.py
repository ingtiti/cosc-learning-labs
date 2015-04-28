# Copyright 2014 Cisco Systems, Inc.
# 
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

from basics.interface_names import interface_names
from basics.interface_configuration import interface_configuration
from settings import config
from unittest.case import TestCase
from unittest import main

class Test(TestCase):

    def test_interface_configuration(self):
        for device_name in config['network_device']:
            interface_name_list = interface_names(device_name)
            for interface_name in interface_name_list:
                info = interface_configuration(device_name, interface_name)
                self.assertEqual(info.name, interface_name)
                self.assertIsNotNone(info.description)
                self.assertIsNotNone(info.address)
                self.assertIsNotNone(info.netmask)

if __name__ == '__main__':
    main()
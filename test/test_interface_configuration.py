# Copyright 2015 Cisco Systems, Inc.
# 
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

from __future__ import print_function
from basics.inventory import inventory_connected, inventory_mounted
from basics.interface import interface_configuration_tuple, interface_names, InterfaceConfiguration
from unittest.case import TestCase
from unittest import main
from helpers import inventory_connect

class Test(TestCase):

    def setUp(self):
        """
        Mount every device that is unmounted and verify the connection to each device. 
        """
        inventory_connect()

    def test_interface_configuration(self):
        device_names = inventory_connected()
        self.assertTrue(device_names, "Expected one or more connected devices.")
        for device_name in device_names:
            interface_name_list = interface_names(device_name)
            for interface_name in interface_name_list:
                info = interface_configuration_tuple(device_name, interface_name)
                self.assertEqual(info.name, interface_name)
                self.assertIsNotNone(info.description)
                self.assertTrue(info.address and info.netmask or not info.address and not info.netmask)

if __name__ == '__main__':
    main()

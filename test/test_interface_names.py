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

from __future__ import print_function
from basics.interface_names import interface_names
from settings import config
from unittest.case import TestCase
from basics.inventory import inventory_connected, inventory_unmounted, device_mount, inventory_mounted
import time
from unittest import main

class Test(TestCase):

    network_device_config = config['network_device']

    def setUp(self):
        unmounted_list = inventory_unmounted()
        for device_name in unmounted_list:
            device_config = self.network_device_config[device_name]
            print('setup: device_mount(' + device_name, *device_config.values(), sep=', ', end=')\n')
            device_mount(
                device_name,
                device_config['address'],
                device_config['port'],
                device_config['username'],
                device_config['password'])
        
        if unmounted_list:
            print('Sleep to allow Controller to update...')
            time.sleep(2)
            self.assertTrue(inventory_mounted(), 'Not mounted: ' + str(inventory_unmounted()))

    def test_interface_names(self):
        for device_name in inventory_connected():
            print('test: interface_names(' + device_name, end=')')
            interfaces = interface_names(device_name)
            print(', got:', *interfaces)
            self.assertGreater(len(interfaces), 1, 'Expected multiple interfaces, got %d' % len(interfaces))

if __name__ == '__main__':
    main()

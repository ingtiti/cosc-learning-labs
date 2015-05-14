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
from basics.inventory import device_dismount, inventory_mounted, inventory_unmounted, device_mount, mounted, device_control
from settings import config
import time
from unittest.case import TestCase
from unittest import main

class Test(TestCase):
    
    network_device_config = config['network_device']

    def setUp(self):
        """
        Mount every device that is unmounted.
        """
        unmounted_list = inventory_unmounted()
        if unmounted_list:
            print('setup:')
            for device_name in unmounted_list:
                device_config = self.network_device_config[device_name]
                print('\tdevice_mount(' + device_name, *device_config.values(), sep=', ', end=')\n')
                device_mount(
                    device_name,
                    device_config['address'],
                    device_config['port'],
                    device_config['username'],
                    device_config['password'])
                self.assertTrue(mounted(device_name), 'Expected mounted: ' + device_name)

    def test_device_dismount(self):
        """
        Apply function device_dismount to every device that is mounted.
        """
        mounted_list = inventory_mounted()
        self.assertTrue(mounted_list, 'One or more devices must be mounted.')
        print('test:')
        for device_name in mounted_list:
            print('\tdevice_dismount(', device_name, end=')\n')
            device_dismount(device_name)
            self.assertFalse(mounted(device_name), 'Expected not mounted: ' + device_name)

if __name__ == '__main__':
    main()

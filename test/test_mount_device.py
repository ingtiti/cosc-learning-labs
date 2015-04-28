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
from basics.inventory import device_mount, inventory_mounted, mounted, device_dismount, inventory_unmounted
from settings import config
import time
from unittest.case import TestCase
from unittest import main

class Test(TestCase):

    network_device_config = config['network_device']

    def setUp(self):
        mounted_list = inventory_mounted()
        for device_name in mounted_list:
            print('setup: device_dismount(' + device_name, end=')\n')
            device_dismount(device_name)
        
        if mounted_list:
            print('Sleep to allow Controller to update...')
            time.sleep(2)
            self.assertFalse(inventory_mounted(), 'Dismount required: ' + str(inventory_mounted()))
            

    def test_mount_device(self):
        self.assertTrue(self.network_device_config, 'One or more devices must be configured.')

        unmounted_list = inventory_unmounted()
        self.assertTrue(unmounted_list, 'One or more devices must be unmounted.')
        for device_name in unmounted_list:
            device_config = self.network_device_config[device_name]
            print('test: device_mount(' + device_name, *device_config.values(), sep=', ', end=')\n')
            device_mount(
                device_name,
                device_config['address'],
                device_config['port'],
                device_config['username'],
                device_config['password'])
            
        print('Sleep to allow Controller to update...')
        time.sleep(2)
        for device_name in unmounted_list:
            self.assertTrue(mounted(device_name), 'Not mounted: ' + device_name)

if __name__ == '__main__':
    main()

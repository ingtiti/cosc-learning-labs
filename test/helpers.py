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

''' 
Helper functions for testing.

@author: Ken Jarrad
'''

from __future__ import print_function as _print_function
from basics.inventory import device_mount, inventory_unmounted, inventory_connected, DeviceControl
from settings import config
import time

def inventory_connect(time_out=10.0, time_interval=0.2):
    """
    Mount all unmounted devices and wait for the (asynchronous) connection to occur.

    Parameters:
    time_out      -- Number of seconds to elapse before time out.
    time_interval -- Initial time interval between checks.
    
    Raise:
    Exception if any connections are not verified during the time allocated.
    """
    unmounted_collection = set(inventory_unmounted())
    if unmounted_collection:
        for device_name in unmounted_collection:
            mount_from_settings(device_name)
        time_accum = 0.0
        num_checks = 0
        while time_accum < time_out:
            num_checks += 1
            expanding_interval = time_interval * num_checks
            time_accum += expanding_interval  
            # Don't hammer the Controller or it will crash.
            # This not a denial-of-service (DOS) attack ;-)
            # Print a message explaining why nothing is happening, otherwise user might terminate.
            print('sleep(%s)' % expanding_interval)
            time.sleep(expanding_interval)
            pending_connection = unmounted_collection - set(inventory_connected())
            if pending_connection:
                print('%s network device(s) pending connection after %s check(s) and %s seconds.' % (len(pending_connection), num_checks, time_accum))
            else:
                print('%s network device connection(s) verified after %s check(s) and %s seconds.' % (len(unmounted_collection), num_checks, time_accum))
                print()
                return
        pending_connection = unmounted_collection - set(inventory_connected())
        if pending_connection:
            raise Exception('Expected connection to device(s): ' + str(*pending_connection))

network_device_dict = config['network_device']

def mount_from_settings(device_name):
    """
    Mount the specified device using the configured settings.
    
    Return a DeviceControl representation of the configured settings.
    """
    device_config = network_device_dict[device_name]
    control = DeviceControl(device_name=device_name, **device_config)
    device_mount(
        control.device_name,
        control.address,
        control.port,
        control.username,
        control.password)
    return control

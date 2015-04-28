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

from basics.inventory import inventory_connected
from basics.interface import management_interface
from basics.interface import interface_names

def sample_device():
    'Return a device_name if possible; otherwise raise LookupError.'
    return sample_interface()[0]

def sample_interface():
    'Return a tuple of (device_name, interface_name) if possible; otherwise raise LookupError.'
    for device_name in inventory_connected():
        print device_name
        management_name = management_interface(device_name)
        print management_name
        if management_name == None:
            continue # Uncertain which interface is for management.
        for interface_name in interface_names(device_name):
            print interface_name
            if interface_name == management_name:
                continue
            return (device_name, interface_name)
    raise LookupError("Unable to find a suitable sample device and interface in the inventory.")

sample_interface()

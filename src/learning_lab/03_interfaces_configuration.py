#!/usr/bin/env python3.4

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

''' Sample usage of function 'interface_configuration'.

    Print the function's documentation then invoke the function and print the output.
    Apply the function to all interfaces on all devices.
    The devices must be connected.
    The interfaces are on the 'data plane' 
    Interfaces on the 'control plane' are excluded.
'''
from __future__ import print_function as _print_function
from pydoc import plain
from pydoc import render_doc as doc
from basics.interface import management_interface
from basics.interface_configuration import interface_configuration
from basics.interface_names import interface_names
from basics.inventory import inventory_connected
from basics.render import print_rich

def demonstrate(device_name, interface_name):
    ''' Apply function 'interface_configuration' to the specified device/interface.'''
    print_rich('  ', interface_configuration(device_name, interface_name))

def main():
    ''' Select a device/interface and demonstrate.'''
    print(plain(doc(interface_configuration)))
    foundInterface = False
    for device_name in sorted(inventory_connected()):
        print("%s:" % device_name)
        mgmt_name = management_interface(device_name)
        for interface_name in sorted(interface_names(device_name)):
            # Choose interface on 'data plane' not 'control plane'.
            if interface_name == mgmt_name:
                continue
            else:
                foundInterface = True
                demonstrate(device_name, interface_name)
        if not foundInterface:
            print("There are no suitable network interfaces for this device.")

if __name__ == "__main__":
    main()

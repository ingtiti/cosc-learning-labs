#!/usr/bin/env python2.7

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

''' Sample usage of function 'static_route_create'.

    Print the function's documentation.
    Apply the function to a network device.
    Print the function output.
'''

from __future__ import print_function as _print_function
from pydoc import plain
from pydoc import render_doc as doc
import os
from basics.inventory import inventory_mounted
from basics.interface import interface_names, management_interface, interface_configuration_tuple
from basics.interpreter import sys_exit
from basics.routes import static_route_create, inventory_static_route, to_ip_network
from importlib import import_module
static_route_fixture = import_module('learning_lab.04_static_route_fixture')

def match(device_name, interface_network):
    """ Discover matching interface on a different device."""
    for other_device in inventory_mounted():
        if other_device == device_name:
            continue
        for interface_name in interface_names(other_device):
            interface_config = interface_configuration_tuple(other_device, interface_name)
            if interface_config.address is None:
                # Skip network interface with unassigned IP address.             
                continue
            other_network = to_ip_network(interface_config.address, interface_config.netmask)
            if other_network == interface_network:
                print('Match %s/%s/%s to %s/%s' % (device_name, interface_config.address, interface_config.netmask, \
                                                   other_device, interface_network))
                return interface_config.address
    return None

def demonstrate(device_name):
    ''' Apply function 'static_route_create' to the specified device for a new destination.'''
    mgmt_name = management_interface(device_name)
    interface_list = interface_names(device_name)
    for interface_name in interface_list:
        if interface_name == mgmt_name:
            # Do not configure static routes on the control plane.             
            continue
        config = interface_configuration_tuple(device_name, interface_name)
        if config.address is None:
            # Skip network interface with unassigned IP address.             
            continue
        print()
        interface_network = to_ip_network(config.address, config.netmask)
        next_hop_address = match(device_name, interface_network)
        if next_hop_address is None:
            print('No end-point for %s/%s/%s/%s' % (device_name, interface_name, config.address, config.netmask))
            continue
        destination_network = static_route_fixture.new_destination(device_name, interface_network)
        print('static_route_create(%s, %s, %s)' % (device_name, destination_network, next_hop_address))
        static_route_create(device_name, destination_network, next_hop_address)
        return True
    return False

def main():
    ''' Select a capable device and demonstrate.'''
    print(plain(doc(static_route_create)))
    print('inventory_static_route()')
    device_names = inventory_static_route()
    print('\t', device_names)
    if not device_names:
        print("There are no 'static route' capable devices to examine. Demonstration cancelled.")
    else:
        for device_name in device_names:
            if demonstrate(device_name):
                return os.EX_OK
    return os.EX_TEMPFAIL

if __name__ == "__main__":
    sys_exit(main())

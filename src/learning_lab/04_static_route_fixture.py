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

""" Data shared by 'static route' sample scripts."""

from basics.routes import  static_route_exists, to_ip_network
from basics.interface import interface_names, management_interface, interface_configuration_tuple

def next_subnet(network):
    """ Determine the next subnet, relative to the specified network. """
    return to_ip_network(network.network_address + 256, 24)

def new_destination(device_name, interface_network):
    """ Determine a static route destination that does not exist on the specified device. """
    destination_network=next_subnet(interface_network)
    while static_route_exists(device_name, destination_network):
        destination_network=next_subnet(destination_network)
    return destination_network

def sample_destination(device_name):
    """ Determine a suitable destination for a static route from the specified network device. """
    # Implementation: use 'next subnet' of any data interface on the specified device.
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
        interface_network = to_ip_network(config.address, config.netmask)
        destination_network = next_subnet(interface_network)
        return destination_network
    return None

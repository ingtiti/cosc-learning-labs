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

""" 
Demonstrate how to determine whether a 'static route' exists on a specific device.
 
Introduce function 'static_route_exists'.
Print the function's documentation.

Use several example destinations, such as 2.2.2.2, 3.3.3.3, etc.
Apply the function to a network device once per example destination.
Print the outcome.
"""

from __future__ import print_function
from collections import OrderedDict
import os
from pydoc import plain
from pydoc import render_doc as doc
from basics.interpreter import sys_exit
from basics.routes import   static_route_exists, inventory_static_route
from basics.render import print_rich
from ipaddress import ip_network

destination_network_list = [
    ip_network(u"%s.%s.%s.%s/255.255.255.255" % (counter, counter, counter, counter), strict=False) 
    for counter in range(2, 6)
]

def demonstrate(device_name):
    """ 
    Apply function 'static_route_exists' to the specified device for each destination in the list.
    """
    for destination_network in destination_network_list:
        print('static_route_exists(%s, %s)' % (device_name, destination_network))
        
    print()
    
    print_rich([OrderedDict([
            ("device", device_name),
            ("destination", destination_network),
            ("exists", str(static_route_exists(device_name, destination_network)))
        ]) for destination_network in destination_network_list
    ])
    return True

def main():
    """
    Print the function's documentation then demonstrate the function multiple times on one device.
    """
    print(plain(doc(static_route_exists)))
    
    print('Determine which devices are capable.')
    print('inventory_static_route()')
    device_names = inventory_static_route()
    print_rich(device_names)
    print()

    print('Static routes to the following destination networks will be queried.')
    print_rich(destination_network_list)
    print()
    
    if not device_names:
        print("There are no 'static route' capable devices to examine. Demonstration cancelled.")
    else:
        for device_name in device_names:
            if demonstrate(device_name):
                return os.EX_OK
    return os.EX_TEMPFAIL

if __name__ == "__main__":
    sys_exit(main())

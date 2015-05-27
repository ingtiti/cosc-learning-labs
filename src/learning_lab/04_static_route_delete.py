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

''' Sample usage of function 'static_route_delete'.

    Print the function's documentation.
    Apply the function to a network device.
    Retry with a different network device/prefix until a route is deleted.
'''

from __future__ import print_function as _print_function
from pydoc import plain
from pydoc import render_doc as doc
import os
from basics.interpreter import sys_exit
from basics.routes import static_route_delete, inventory_static_route,\
    static_route_list

def demonstrate(device_name):
    ''' Apply function 'static_route_delete' to any route of the specified device.'''
    print()
    print('static_route_list(' + device_name, sep=', ', end=')\n')
    route_list=static_route_list(device_name)
    print('\t', [str(route) for route in route_list])
    for destination_network in route_list:
        print()
        print('static_route_delete(' + device_name, destination_network, sep=', ', end=')\n')
        static_route_delete(device_name, destination_network)
        return True
    return False

def main():
    ''' Select a device and demonstrate. Retry with a different device/route until information is deleted.'''
    print(plain(doc(static_route_delete)))
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

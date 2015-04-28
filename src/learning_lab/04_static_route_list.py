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

''' Sample usage of function 'static_route_list'.

    Print the function's documentation.
    Apply the function to a network device.
    Print the function output.
    If no routes are found then retry with a different network device.
'''

from __future__ import print_function as _print_function
import os
from pydoc import plain
from pydoc import render_doc as doc
from basics.interpreter import sys_exit
from basics.routes import static_route_list, inventory_static_route

def demonstrate(device_name):
    ''' Apply function 'static_route_list' to the specified device.
    
        Return True when one or more routes are found.
    '''
    print('static_route_list(' + device_name, end=')\n')
    routes = static_route_list(device_name)
    print('\t', [str(route) for route in routes])
    return bool(routes)

def main():
    """ Select a device and demonstrate. If no information is found then retry with a different device."""
    print(plain(doc(static_route_list)))
    device_names = inventory_static_route()
    if not device_names:
        print("There are no 'static route' capable devices to examine. Demonstration cancelled.")
    else:
        for device_name in device_names:
            if demonstrate(device_name):
                return os.EX_OK
    return os.EX_TEMPFAIL

if __name__ == "__main__":
    sys_exit(main())

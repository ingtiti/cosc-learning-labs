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

''' Sample usage of function 'static_route_exists'.

    Print the function's documentation.
    Apply the function to a network device for one or more sample 'static route' destinations.
    Print the function output.
'''

from __future__ import print_function as _print_function
import os
from pydoc import plain
from pydoc import render_doc as doc
from basics.interpreter import sys_exit
from basics.routes import   static_route_exists, inventory_static_route
from importlib import import_module
static_route_fixture = import_module('learning_lab.04_static_route_fixture')

def demonstrate(device_name):
    ''' Apply function 'static_route_exists' to one or more static route destinations for the specified device.'''
    destination_network = static_route_fixture.sample_destination(device_name)
    print()
    print('static_route_exists(' + device_name, destination_network, sep=', ', end=')\n')
    print('\t', static_route_exists(device_name, destination_network))
    return True

def main():
    ''' Select a device and demonstrate for each potential static route prefix.'''
    print(plain(doc(static_route_exists)))
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

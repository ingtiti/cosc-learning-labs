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

''' Sample usage of function 'static_route_json'.

    Print the function's documentation.
    Apply the function to a network device and static route destination.
    Print the function output.
    Retry with a different network device if no information found.
'''

from __future__ import print_function as _print_function
from pydoc import plain
from pydoc import render_doc as doc
import os
from basics.interpreter import sys_exit
from basics.routes import static_route_json, inventory_static_route
import json
from importlib import import_module
static_route_fixture = import_module('learning_lab.04_static_route_fixture')

def demonstrate(device_name):
    ''' Apply function 'static_route_json' to the specified device for a sample destination.'''
    print()
    destination_network = static_route_fixture.sample_destination(device_name)
    print('static_route_json(' + device_name, destination_network, sep=', ', end=')\n')
    route = static_route_json(device_name, destination_network)
    if route:
        print(json.dumps(route, indent=2, sort_keys=True))
    else:
        print('\t', route)
    return route is not None

def main():
    ''' Select a device and demonstrate on potential routes, repeat until information found.'''
    print(plain(doc(static_route_json)))
    inventory = inventory_static_route()
    if not inventory:
        print("There are no 'static route' capable devices to examine. Demonstration cancelled.")
    else:
        for device_name in inventory:
            if demonstrate(device_name):
                return os.EX_OK
    return os.EX_TEMPFAIL

if __name__ == "__main__":
    sys_exit(main())

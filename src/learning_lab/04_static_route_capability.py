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
Demonstrate how to identify network devices that have 'static route' capabilities.

If there are no such devices then all sample scripts prefixed with 
`04_static_route` are unable to perform their demonstrations.

Introduce function 'inventory_static_route'.
Print the function's documentation. 

Apply the function to the inventory of network devices.
Print the function output.
"""

from __future__ import print_function
from pydoc import plain
from pydoc import render_doc as doc
from basics.interpreter import sys_exit, EX_OK, EX_TEMPFAIL
from basics.routes import inventory_static_route
from basics.render import print_table

def demonstrate():
    """
    Apply function 'inventory_static_route' to the inventory of network devices.
    """
    print('inventory_static_route()')
    device_names = inventory_static_route()
    print_table(device_names, headers=('device-name',))
    return device_names
    
def main():
    """
    Print the function documentation then demonstrate the function usage.
    """
    print(plain(doc(inventory_static_route)))
    
    return EX_OK if demonstrate() else EX_TEMPFAIL

if __name__ == "__main__":
    sys_exit(main())

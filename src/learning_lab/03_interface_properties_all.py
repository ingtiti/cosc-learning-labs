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
Demonstrate how to get the properties of all network interfaces on a network device.

Introduce function 'interface_properties'.
Print the function's documentation.

Select any network device that is capable.
Apply the function to the selected device.
Print the function output.
"""
from __future__ import print_function

from pydoc import plain
from pydoc import render_doc as doc

from basics.interface_properties import interface_properties
from basics.inventory import inventory_connected
from basics.render import print_rich
from basics.interpreter import sys_exit
import os

def demonstrate(device_name):
    """
    Apply function 'interface_properties' to the specified device.
    """
    print('interface_properties(%s)' % device_name)
    print_rich(interface_properties(device_name))

def main():
    """
    Print the function's documentation then demonstrate usage of the function on one device.
    """
    print(plain(doc(interface_properties)))

    for device_name in inventory_connected():
        demonstrate(device_name)
        return os.EX_OK
    print("There are no suitable network devices and interfaces. Demonstration cancelled.")
    return os.EX_TEMPFAIL

if __name__ == "__main__":
    sys_exit(main())

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

''' Sample usage of function 'capability'.

   For each connected device, get the capabilities for that device and print the 
   device name and capability.
'''

from __future__ import print_function as _print_function
from basics.inventory import  inventory_connected
from basics.inventory import capability

def main():
    for device_name in inventory_connected():
        for capability_name in capability(device_name):
            print(device_name, capability_name)

if __name__ == "__main__":
    main()
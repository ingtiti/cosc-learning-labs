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

''' 
    Display a table of capability rows and device columns.
    This is a WIP as we need a HTML table output to make this work visually. TODO
'''

from __future__ import print_function as _print_function
# from basics.capability import capability
from basics.inventory import  inventory_connected
from basics.inventory import capability
# from basics.capability import capability as capabilityx
# from basics.inventory import  inventory_mounted
import re
# from collections import OrderedDict

_qualified_name = re.compile(r'\((.*)\)(.*)')
_revision = re.compile(r'(.*)\?revision=(.*)')

def capability_matrix(devices):
    capability_names = set()
    capability_by_device = {}
    for device_name in devices:
        capability_revision_by_name = {}
        for capability_entire in capability(device_name):
            match = _qualified_name.match(capability_entire)
            qualifier = match.group(1)
            capability_name = match.group(2)
            capability_names.add(capability_name)
            match = _revision.match(qualifier)
            # ns = match.group(1)  # namespace ignored at present.
            revision = match.group(2)
            capability_revision_by_name[capability_name] = revision
        capability_by_device[device_name] = capability_revision_by_name
    
    # The 2 dimensional 'matrix' data structure.         
    device_by_capability = {}
    
    # Initialise dict with capability name as 'key' and empty list as 'value'.     
    for capability_name in capability_names:
        device_by_capability[capability_name] = []
        
    # Populate 'device' dimension per capability with the revision of each device.   
    for capability_name in capability_names:
        revision_per_device = device_by_capability[capability_name]
        for device in devices:
            capability_revision_by_name = capability_by_device[device]
            revision_per_device.append(capability_revision_by_name[capability_name] if capability_name in capability_revision_by_name else None)

    return device_by_capability

devices = []
device_by_capability = {}

def main():
    global devices
    devices = sorted(inventory_connected())
    
    global device_by_capability
    device_by_capability = capability_matrix(devices)
    
#     print(devices)
#     for capability_name in sorted(device_by_capability.keys()):
#         revision_list = device_by_capability[capability_name]
#         print(capability_name, revision_list)

if __name__ == "__main__":
    main()
    print(len(device_by_capability))
    print('devices:',devices)
#     for capability_name in sorted(device_by_capability.keys()):
#         print(capability_name, device_by_capability[capability_name])
    print (*device_by_capability.items(),sep='\n')
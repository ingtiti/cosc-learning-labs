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
    Display a matrix of capability rows and device columns.
    This is a WIP as we need a HTML table output to make this work visually. TODO
'''

from __future__ import print_function as _print_function
# from basics.capability import capability
from basics.inventory import  inventory_connected
from basics.inventory import capability
# from basics.capability import capability as capabilityx
# from basics.inventory import  inventory_mounted
import re
from collections import OrderedDict

_qualified_name = re.compile(r'\((.*)\)(.*)')
_revision = re.compile(r'(.*)\?revision=(.*)')

def capability_matrix(devices):
    capability_ids = set()
    capability_by_device = {}
    for device_name in devices:
        capability_revision_by_id = {}
        for capability_entire in capability(device_name):
            match = _qualified_name.match(capability_entire)
            qualifier = match.group(1)
            capability_name = match.group(2)
            match = _revision.match(qualifier)
            
            # namespace
            ns = match.group(1)
            # truncate redundant information
            ns = ns[:-len(capability_name)] if ns.endswith(capability_name) else ns
            
            revision = match.group(2)
            capability_id = (capability_name, ns)
            capability_ids.add(capability_id)
            capability_revision_by_id[capability_id] = revision
        capability_by_device[device_name] = capability_revision_by_id
    
    # The 2 dimensional 'matrix' data structure.
    # Each capability is a 'key' with a vector as 'value'.         
    device_by_capability = OrderedDict()
    
    # Initialise 'capability' dimension and set 'device' dimension to empty vector.      
#     for capability_id in sorted(capability_ids):
#         device_by_capability[capability_id] = []
        
    # Populate 'device' dimension per capability with the revision of each device.   
    for capability_id in capability_ids:
        revision_per_device = []
        for device in devices:
            capability_revision_by_id = capability_by_device[device]
            revision_per_device.append(capability_revision_by_id[capability_id] if capability_id in capability_revision_by_id else None)
        device_by_capability[capability_id] = revision_per_device
        
    return device_by_capability

devices = []
matrix = {}

def main():
    global devices
    devices = sorted(inventory_connected())
    
    global matrix
    matrix = capability_matrix(devices)
    
#     print(devices)
#     for capability_name in device_by_capability.keys():
#         revision_list = device_by_capability[capability_name]
#         print(capability_name, revision_list)

if __name__ == "__main__":
    main()
    print('devices:', devices)
    print (*matrix.items(), sep='\n')

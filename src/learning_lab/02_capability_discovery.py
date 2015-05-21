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

''' Example code to discover devices that have a specific capability.
'''

from __future__ import print_function as _print_function
from basics.inventory import  capability_discovery

from basics.acl import capability_name as acl_capability_name
from basics.acl import capability_ns as acl_capability_ns

from basics.routes import capability_name as static_route_capability_name
from basics.routes import capability_ns as static_route_capability_ns

def demonstrate(capability_name, capability_namespace):
    print()
    print('capability_discovery(%s, %s)' % (capability_name, capability_namespace), end=':\n')
    capable_list = capability_discovery(capability_name, capability_namespace)
    if not capable_list:
        print('\t',None)
    else:
        for capable in capable_list:
            print('\t', capable[0], capable[1][2])
    
def main():
    demonstrate(acl_capability_name, acl_capability_ns)
    demonstrate(static_route_capability_name, static_route_capability_ns)
    demonstrate('not_available_yet', 'coming_soon')

if __name__ == "__main__":
    main()

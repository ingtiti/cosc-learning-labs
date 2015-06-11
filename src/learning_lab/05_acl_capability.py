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
Demonstrate how to identify network devices that have 'access control list' capabilities.

If there are no such devices then all sample scripts prefixed with 
`05_acl` are unable to perform their demonstrations.
"""

from __future__ import print_function
from pydoc import plain
from pydoc import render_doc as doc
from basics.interpreter import sys_exit, EX_OK, EX_TEMPFAIL
from basics.acl import capability_ns, capability_name
from basics.inventory import capability_discovery, inventory_mounted, connected
from basics.render import print_table

def demonstrate(device_name):
    ''' Apply function 'capability_discovery' to the specified device for required capability. '''
    print('capability_discovery(device_name=%s, capability_name=%s, capability_ns=%s)' % (device_name, capability_name, capability_ns))
    results = capability_discovery(device_name=device_name, capability_name=capability_name, capability_ns=capability_ns)
    print_table([{'device-name' : result[0], 'capability' : result[1][0], 'namespace' : result[1][1], 'revision' : result[1][2]} for result in results])
    return bool(results)

def main():
    ''' Document and demonstrate the function until a capable device is found.'''
    print(plain(doc(capability_discovery)))
    for device_name in inventory_mounted():
        try:
            if demonstrate(device_name):
                return EX_OK
        except Exception as e:
            if connected(device_name):
                # Unexplained exception.                
                print(e)
                return EX_TEMPFAIL
            else:
                # Expect exception when device not connected.             
                print('connected(%s): False' % device_name)
    return EX_TEMPFAIL

if __name__ == "__main__":
    sys_exit(main())

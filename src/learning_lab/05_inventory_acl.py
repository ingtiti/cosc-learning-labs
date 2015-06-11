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

''' Sample usage of function 'inventory_acl'.

    Print the function's documentation.
    Apply the function.
    Print the function output.
'''

from __future__ import print_function as _print_function
from pydoc import plain
from pydoc import render_doc as doc
from basics.interpreter import sys_exit, EX_OK, EX_TEMPFAIL
from basics.acl import inventory_acl

def demonstrate():
    ''' Apply function 'inventory_acl'.
    
        Return True if network devices are discovered.
    '''
    print('inventory_acl()')
    print(inventory_acl())

def main():
    ''' Document and demonstrate the function.'''
    print(plain(doc(inventory_acl)))
    if demonstrate():
        return EX_OK
    else:
        return EX_TEMPFAIL

if __name__ == "__main__":
    sys_exit(main())

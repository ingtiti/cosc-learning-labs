#!/usr/bin/env python

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

# This code uses https://github.com/pexpect/pexpect. The pexpect licence is below:

'''
PEXPECT LICENSE

    This license is approved by the OSI and FSF as GPL-compatible.
        http://opensource.org/licenses/isc-license.txt

    Copyright (c) 2012, Noah Spurrier <noah@noah.org>
    PERMISSION TO USE, COPY, MODIFY, AND/OR DISTRIBUTE THIS SOFTWARE FOR ANY
    PURPOSE WITH OR WITHOUT FEE IS HEREBY GRANTED, PROVIDED THAT THE ABOVE
    COPYRIGHT NOTICE AND THIS PERMISSION NOTICE APPEAR IN ALL COPIES.
    THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
    WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
    MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
    ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
    WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
    ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
    OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

    This script will use telnet to login to a Cisco XRv device and set the cryptographic keys to support SSH connectivity.
'''

from __future__ import print_function

from __future__ import absolute_import

import pexpect
import sys

def main ():
    
    telnet_command = "telnet %s" % '172.16.1.11'
    child = pexpect.spawn (telnet_command) 
    child.logfile = sys.stdout
    child.expect ('Username:')
    child.sendline ('cisco')
    child.expect ('Password:')
    child.sendline ('cisco')
    child.expect ('#')
    child.sendline ('crypto key generate dsa')
    index = child.expect (['[yes/no]','1024]'])
    if index == 0:
        child.sendline ('yes')
        child.expect ('1024]')
        child.sendline ('')
    elif index == 1:
        child.sendline ('')
        
if __name__ == '__main__':

    main ()

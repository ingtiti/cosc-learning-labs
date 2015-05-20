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
    Connects to the controller and authenticates, as a basic sanity check that the controller is reachable and responding to requests.
'''

from __future__ import print_function as _print_function
import settings
from basics.odl_http import coordinates as odl_coordinates, odl_http_head
from sys import stderr
from basics.interpreter import sys_exit
import os

if __name__ == "__main__":
    # Controller end-point
    print('odl_url_prefix:', odl_coordinates.url_prefix)
    print('odl_username:', odl_coordinates.username)
    print('odl_password:', odl_coordinates.password)
    
    try:
        response = odl_http_head(
            url_suffix='operational/opendaylight-inventory:nodes',
            accept='application/json',
            expected_status_code=[200, 404, 503])
        print('status code:', response.status_code)
        if response.status_code == 404:
            print('status: not found (either the URL is incorrect or the controller is starting).')
            print('url:', response.url)
        elif response.status_code == 503:
            print('status: service unavailable (allow 5 or 10 minutes for controller to become ready)')
        else:
            print('status: OK')
        exit_code = os.EX_OK
    except Exception as e:
        exit_code = os.EX_CONFIG
        raise e
    finally:
        sys_exit(exit_code)


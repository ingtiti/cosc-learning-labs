# Copyright 2014 Cisco Systems, Inc.
# 
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

try:
    from urllib import quote_plus
except ImportError:
    from urllib.parse import quote_plus
from basics.odl_http import odl_http_delete

_url_template = 'config/opendaylight-inventory:nodes/node/controller-config/yang-ext:mount/config:modules/module/%s'

def dismount_device(
    device_name
):
    'Dismount a network device that has been mounted on the ODL server.'
    url_suffix = _url_template % quote_plus(device_name)
    odl_http_delete(url_suffix)

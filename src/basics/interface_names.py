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

from lxml import etree
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from basics.odl_http import odl_http_get
try:
    from urllib import quote_plus
except ImportError:
    from urllib.parse import quote_plus

_url_template = 'operational/opendaylight-inventory:nodes/node/%s/yang-ext:mount/Cisco-IOS-XR-ifmgr-oper:interface-properties'

def interface_names(device_name):
    'Return a list of interface names, given the name of a mounted, connected device.'
    url_suffix = _url_template % quote_plus(device_name)
    response = odl_http_get(url_suffix, 'application/xml', expected_status_code=[200, 400])
    if response.status_code == 400:
        return []  # The inventory item does not have interfaces.
    tree = etree.parse(StringIO(response.text))
    namespace = tree.getroot().tag[1:].split("}")[0]
    ns = {'n':namespace}
    return tree.xpath(".//n:system-view//n:interface[n:encapsulation/text()='ether']/n:interface-name/text()", namespaces=ns)

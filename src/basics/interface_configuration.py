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

try:
    from urllib import quote_plus
except ImportError:
    from urllib.parse import quote_plus
from collections import namedtuple
from basics.odl_http import odl_http_get
from basics.odl_http import odl_http_put
import json

_url_template = 'config/opendaylight-inventory:nodes/node/%s/yang-ext:mount/Cisco-IOS-XR-ifmgr-cfg:interface-configurations/interface-configuration/%s/%s'

InterfaceConfiguration = namedtuple('InterfaceConfiguration', ['name', 'description', 'shutdown', 'address', 'netmask', 'ipv4_packet_filter_outbound', 'ipv4_packet_filter_inbound', 'active'])

def interface_configuration(
    device_name,
    interface_name
):
    'Return a named tuple containing the information available for the specified interface of the specified, mounted device.'
    url_suffix = _url_template % (device_name, 'act', quote_plus(interface_name))
    response = odl_http_get(url_suffix, 'application/xml')
    tree = etree.parse(StringIO(response.text))
    result = InterfaceConfiguration(
        name=tree.findtext('{*}interface-name'),
        description=tree.findtext('{*}description'),
        ipv4_packet_filter_outbound=tree.findtext('//{*}ipv4-packet-filter/{*}outbound/{*}name'),
        ipv4_packet_filter_inbound=tree.findtext('//{*}ipv4-packet-filter/{*}inbound/{*}name'),
        active=tree.findtext('{*}active'),
        shutdown=tree.find('{*}shutdown') != None,
        address=tree.findtext('//{*}primary/{*}address'),
        netmask=tree.findtext('//{*}primary/{*}netmask'))
    return result

_request_content_template = '''
{
  "interface-configuration": [
    {
      "active": "%s",
      "Cisco-IOS-XR-ipv4-io-cfg:ipv4-network": {
        "addresses": {
          "primary": {
            "netmask": "%s", 
            "address": "%s"
          }
        }
      },%s
      "interface-name": "%s", 
      "description": "%s"
    }
  ]
}
'''

def interface_configuration_update(
    device_name,
    interface_name,
    description,
    address,
    netmask,
    active='act',
    shutdown=False
):
    '''Update the configuration of the specified interface of the specified device.
    
    The outcome is undefined if the specified device is not connected. 
    '''
    url_suffix = _url_template % (device_name, active, quote_plus(interface_name))
    shutdownField = '\n"shutdown" : "",' if shutdown else ""
    request_content = _request_content_template % (active, netmask, address, shutdownField, interface_name, description)
    odl_http_put(url_suffix, 'application/json', request_content, expected_status_code=200)

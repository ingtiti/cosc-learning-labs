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
from basics.odl_http import odl_http_post, odl_http_get, odl_http_delete

_request_content_template = '''<?xml version="1.0" encoding="UTF-8"?>
<module xmlns="urn:opendaylight:params:xml:ns:yang:controller:config">
    <type
        xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">prefix:sal-netconf-connector</type>
    <name>%s</name>
    <address
        xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">%s</address>
    <port
        xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">%s</port>
    <username
        xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">%s</username>
    <password
        xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">%s</password>
    <tcp-only
        xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">false</tcp-only>
    <event-executor
        xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">
        <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:netty">prefix:netty-event-executor</type>
        <name>global-event-executor</name>
    </event-executor>
    <binding-registry
        xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">
        <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:md:sal:binding">prefix:binding-broker-osgi-registry</type>
        <name>binding-osgi-broker</name>
    </binding-registry>
    <dom-registry
        xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">
        <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:md:sal:dom">prefix:dom-broker-osgi-registry</type>
        <name>dom-broker</name>
    </dom-registry>
    <client-dispatcher
        xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">
        <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:config:netconf">prefix:netconf-client-dispatcher</type>
        <name>global-netconf-dispatcher</name>
    </client-dispatcher>
    <processing-executor
        xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">
        <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:threadpool">
            prefix:threadpool</type>
        <name>global-netconf-processing-executor</name>
    </processing-executor>
</module>
'''

_bgp_url_suffix = 'config/opendaylight-inventory:nodes/node/controller-config/yang-ext:mount/config:modules'

_dismount_url_suffix_template = 'config/opendaylight-inventory:nodes/node/controller-config/yang-ext:mount/config:modules/module/odl-sal-netconf-connector-cfg:sal-netconf-connector/%s'

def mount_device(
    device_name,
    device_address,
    device_port,
    device_username,
    device_password
):
    request_content = _request_content_template % (device_name, device_address, device_port, device_username, device_password)
    odl_http_post(_bgp_url_suffix, 'application/xml', request_content)

def dismount_device(
    device_name
):
    'Dismount a network device that has been mounted on the ODL server.'
#     request_content = _request_content_template % (device_name, device_address, device_port, device_username, device_password)
#     request_content = _request_content_template % (quote_plus(device_name), 'dummy_address', 'dummy_port', 'dummy_username', 'dummy_password')
    dismount_url_suffix = _dismount_url_suffix_template % device_name
    print odl_http_get(dismount_url_suffix, 'application/xml', expected_status_code=200).text
    odl_http_delete(dismount_url_suffix, 'application/xml', expected_status_code=200)
    print odl_http_get(dismount_url_suffix, 'application/xml', expected_status_code=200).text

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

from __future__ import print_function
from ipaddress import ip_network, _BaseNetwork
from basics.odl_http import odl_http_get, odl_http_post, odl_http_delete
from basics.inventory import capability_discovery
from basics.acl import _error_message

_bgp_url_suffix = 'operational/bgp-rib:bgp-rib/rib/example-bgp-rib/loc-rib/tables/bgp-linkstate:linkstate-address-family/bgp-linkstate:linkstate-subsequent-address-family'

_static_route_url_template = 'config/opendaylight-inventory:nodes/node/{node-id}/yang-ext:mount/Cisco-IOS-XR-ip-static-cfg:router-static/default-vrf/address-family/vrfipv4/vrf-unicast/vrf-prefixes'

_static_route_uni_url_template = _static_route_url_template + '/vrf-prefix/{ip-address}/{prefix-length}'

capability_ns = 'http://cisco.com/ns/yang/'
capability_name = 'Cisco-IOS-XR-ip-static-cfg'

def routes():
    'Request the routes from the ODL server.'
    response = odl_http_get(_bgp_url_suffix, accept='application/json')
    return response.json()

def inventory_static_route(capability_revision=None, device_name=None):
    """ Determine which devices have 'static route' capability.
    
        A specific revision of the capability is optional.
        The discovery process can be scoped to a single device.
        Returns a list of device names. 
    """
    discovered = capability_discovery(
        capability_name=capability_name,
        capability_ns=capability_ns,
        capability_revision=capability_revision,
        device_name=device_name)
    return [device_capability[0] for device_capability in discovered]

def static_route_json_all(device_name):
    '''All static routes on the specified network device.'''
    response = odl_http_get(_static_route_url_template, {'node-id' : device_name}, 'application/json', expected_status_code=[200, 404])
    if response.status_code == 404:
        return []
    else:
        return response.json()['vrf-prefixes']['vrf-prefix']

def to_ip_network(destination_address, destination_mask=None):
    """ Transform various input patterns to a consistent output pattern.
    
    Accepts one of:
        (IPv4Network, None)
        (IPv6Network, None)
        ("1.2.3.4", N)
        ("1.2.3.4/N", None)
        ("1.2.3.4", "255.255.255.0") 
        ("1.2.3.4/255.255.255.0", None) 
            
    Returns:
        An IPv4Network or IPv6Network object.
    """
    if destination_mask is None:
        if isinstance(destination_address, str):
            assert '/' in destination_address
            return ip_network(destination_address, strict=False)
        elif isinstance(destination_address, _BaseNetwork):
            return destination_address
        else:
            raise ValueError('Expected IPv4Network or IPv6Network or string, got %s' % type(destination_address))
    else:
        network = ip_network(u'%s/%s' % (destination_address, destination_mask), strict=False)
        assert str(network).count('/') == 1
        return network

def static_route_json(device_name, destination_network):
    """ JSON representation of the specified 'static route' on the specified network device.
    
        Return None if not found.
    """
    assert isinstance(destination_network, _BaseNetwork)
    url_params = {
        'node-id' : device_name, 
        'ip-address' : destination_network.network_address, 
        'prefix-length' : destination_network.prefixlen
    }
    response = odl_http_get(_static_route_uni_url_template, url_params, 'application/json', expected_status_code=[200, 404])
    if response.status_code == 404:
        return None
    else:
        return response.json()['vrf-prefix'][0]

def static_route_exists(device_name, destination_network):
    """ Determine whether the specified 'static route' exists on the specified device. """
    assert isinstance(destination_network, _BaseNetwork)
    url_params = {
        'node-id' : device_name, 
        'ip-address' : destination_network.network_address, 
        'prefix-length' : destination_network.prefixlen
    }
    response = odl_http_get(_static_route_uni_url_template, url_params, 'application/json', expected_status_code=[200, 404])
    return response.status_code == 200

def static_route_list(device_name):
    """ List the destination network of all 'static routes' on the specified device."""
    route_list = static_route_json_all(device_name)
    print(route_list)
    return [to_ip_network(route['prefix'], route['prefix-length']) for route in route_list]

def static_route_delete(device_name, destination_network):
    """ Delete the specified 'static route' from the specified device.
    
        No value is returned.
        An exception is raised if the static route does not exist on the device.
    """
    assert isinstance(destination_network, _BaseNetwork)
    url_params = {
        'node-id' : device_name, 
        'ip-address' : destination_network.network_address, 
        'prefix-length' : destination_network.prefixlen
    }
    response = odl_http_delete(_static_route_uni_url_template, url_params, expected_status_code=[200, 500])
    if response.status_code != 200:
        raise Exception(_error_message(response.json()))

def static_route_create(device_name, destination_network, next_hop_address, description=None):
    """ Create the specified 'static route' on the specified network device. """
    next_hop = {"next-hop-address" : str(next_hop_address)}
    if description:
        next_hop["description"] = description

    request_content = {
        "Cisco-IOS-XR-ip-static-cfg:vrf-prefix": [
            {
                "prefix" : str(destination_network.network_address),
                "prefix-length": destination_network.prefixlen,
                "vrf-route" : {
                    "vrf-next-hops" : {
                        "next-hop-address" : [next_hop]
                    }
                }
            }
        ]
    }
    response = odl_http_post(_static_route_url_template, {'node-id' : device_name}, 'application/json', request_content, expected_status_code=[204, 409])
    if response.status_code == 409:
        try:
            raise ValueError(response.json()['errors']['error'][0]['error-message'])
        except IndexError:
            pass
        except KeyError:
            pass
        raise ValueError('Already exists: static route to destination network %s on device %s' % (destination_network, device_name))

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

''' Obtain settings by dynamically loading a configuration module located in package 'settings'.

    The configuration module is a normal Python module.
    The configuration module is located in package 'settings' (this package).
    The configuration module must have a variable named 'config', 
    The name of the configuration module is determined by environment variable NETWORK_PROFILE.
    The default configuration module is 'learning_lab.py'.
    The variable named 'config' in the configuration modules is assigned to the
    variable named 'config' in package 'settings' (this package).
    That is:
        settings.config = settings.<configuration_module>.config
    This redirection provides independence.
    Configuration data is accessed in a consistent manner (from 'settings.config').
    Sample Usage:
        import settings
        print(settings.config['odl_server']['address'])
'''

from __future__ import print_function as _print_function
from importlib import import_module
from os import getenv

_network_profile = getenv('NETWORK_PROFILE', 'learning_lab')

try:
    network_settings_module = import_module('settings.' + _network_profile)
except ImportError:
#     print('Failed to import module:', 'settings.' + _network_profile)
#     network_settings_module = empty
    raise
except Exception as e:
    raise ImportError('Unable to import settings.'+ _network_profile, e)

# TODO fill in missing fields with default values, such as Netconf port 830.

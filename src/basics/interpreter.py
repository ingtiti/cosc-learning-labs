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

""" Layer of abstraction that represents any concrete interpreter such as iPython. 

    See also: https://www.artima.com/weblogs/viewpost.jsp?thread=4829 
    for example from Mr Python on how main() should return exit codes.
    
    See also: os.os.EX_OK and other exit code constants.
"""

from __future__ import print_function as _print_function
import os
import sys

def sys_exit(code):
    """Swallow the SystemExit exception if it would adversely impact the interpreter."""
    try:
        global __IPYTHON__
        __IPYTHON__
        if code == os.EX_OK:
            # No need to print anything or raise exception.
            pass
        else:
            # Do not raise exception because iPython halts processing of the notebook.
            print('exit code', code, file=sys.stderr)
    except NameError:
        # System exit raises an exception which seems overkill but is the standard.
        sys.exit(code)

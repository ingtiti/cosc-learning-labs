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

''' Convenience functions to display rich text, such as HTML.

    This module detects the display mode, which is normally 'plain' but can be 'rich'.
    The 'rich' mode recognises the iPython type 'DisplayObject'.
    The 'rich' mode converts types 'list', 'tuple' and 'dict' to HTML TABLE.
    The 'plain' mode delegates to built-in function 'print'.
    
    When this module is imported into iPython it delegates to function 'display';
    otherwise output is printed to stdout using the built-in 'print' function. 
'''

from __future__ import print_function as _print_function
try:
    from IPython.display import display
    from IPython.core.display import DisplayObject, HTML
except ImportError:
    display = print
    class DisplayObject(object):
        def __init__(self, data=None):
            self.data = data
    class HTML(DisplayObject):
        pass

def _display_stdout(value, **kwargs):
    if isinstance(value, DisplayObject):
        print(value.data, **kwargs)
    else:
        print(value, **kwargs)

_display = _display_stdout

def _html_headings(columns):
    return ''.join(['<th>%s</th>' % k for k in columns])
    
def _html_cells(columns):
    return ''.join(['<td>%s</td>' % v for v in columns])

def _html_rows(rows):
    first = rows[0]
    if hasattr(first, '__dict__'):
        r = []
        r.append('<tr>%s</tr>' % _html_headings(vars(first).keys()))
        for row in rows:
            r.append('<tr>%s</tr>' % _html_cells(vars(row).values()))
        return "\n".join(r)
    else:
        return "\n".join(['<tr><td>%s</td></tr>' % str(v) for v in rows])

def _html_matrix(value):
    return HTML('<table>\n%s\n</table>' % _html_rows(value))

def _html_entries(value):
    return "\n".join(['<tr><th>%s</th><td>%s</td></tr>' % (str(k), str(v)) for (k, v) in value.items()])

def _html_dict(value):
    return HTML('<table>\n%s\n</table>' % _html_entries(value))

def _display_rich(*args, **kwargs):
    ''' Display rich text, such as HTML

    This function recognises type 'DisplayObject' as 'rich'.
    Types 'list', 'dict' and 'tuple' and are converted to type 'DisplayObject'.
    Function 'display' is applied to 'DisplayObject'.
    Other types, including 'string', are printed by applying the built-in 'print' function.
    '''
    if len(args) > 1:
        any_rich = False
        for arg in args:
            if isinstance(arg, DisplayObject):
                any_rich = True
        if any_rich:
            # Display each arg separately.
            for arg in args:
                _display_rich(arg, **kwargs)
        else:
            _display(_html_matrix(args))
    elif len(args) == 1:
        arg = args[0]
        if isinstance(arg, DisplayObject):
            _display(arg)
        elif hasattr(arg, '__dict__'):
            entries = vars(arg)
            _display(_html_dict(entries))
        elif isinstance(arg, (list, tuple)):
            _display(_html_matrix(arg))
        else:
            print(arg, **kwargs)

def _print_plain(*args, **kwargs):
    ''' Print plain text

    This function differs from the built-in 'print' function by accepting exactly one parameter,
    to which it applies the built-in 'print' function.
    '''
    print(*args, **kwargs)

print_rich = _print_plain

try:
    __IPYTHON__
    print_rich = _display_rich
    _display = display
except NameError:
    pass

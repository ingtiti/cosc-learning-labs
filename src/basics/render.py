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

from __future__ import print_function
from tabulate import tabulate
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
    if len(rows) == 0:
        return '<tr><td><em>Empty</em></td></tr>'
    peek = rows[0]
    if hasattr(peek, '__dict__'):
        r = []
        r.append('<tr>%s</tr>' % _html_headings(vars(peek).keys()))
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

def _plain_tabulate_dict(arg):
    """
    Return textual representation of dict as table layout.
    
    Table design:             
    - one table row for each field of dict.
    - each row has columns 'field' and 'value'.
    """
    assert isinstance(arg, dict)
    return tabulate([[field, value] for field, value in arg.items()], headers=('name', 'value'))

# Sequence types that 'tabulate' recognises. 
# There may be additional types related to 3rd party libraries.
_columnar = (list, dict, tuple)

def _print_plain_table(*args, **kwargs):
    '''
    Print the arguments in a tabular format using plain text.
    '''
    if len(args) == 1:
        arg = args[0]
        if isinstance(arg, tuple):
            if '_asdict' in dir(arg):
                # title of table is name of type.             
                table_title = type(arg).__name__
                print(table_title)
                print(_plain_tabulate_dict(arg._asdict()))                 
            else:
                _print_plain_table(*arg, **kwargs)
        elif isinstance(arg, list):
            _print_plain_table(*arg, **kwargs)
        elif isinstance(arg, dict):
            print(_plain_tabulate_dict(arg))                 
        else:
            assert arg is not None
            print(tabulate([[arg]], **kwargs))
    elif args:
        peek = args[0]
        headers = _vectorise(kwargs['headers']) \
            if 'headers' in kwargs else "keys" \
            if isinstance(peek, dict) or isinstance(peek, tuple) and '_asdict' in dir(peek) \
            else ()
        # Transform a 1D table to 2D by making each row into a list.         
        args = [arg if isinstance(arg, _columnar) else [arg] for arg in args]
        print(tabulate(args, headers=headers))
    else:
        assert args is None or len(args) == 0
        print(tabulate([[str(None)]], **kwargs))

def _vectorise(arg):
    """
    If arg is scalar then transform to a vector.
    
    A string is considered scalar by this module.
    Note that Python considers strings to be a sequence.
    """
    return arg if isinstance(arg, (tuple, list, dict)) else [arg]

print_table = _print_plain_table

try:
    __IPYTHON__
    print_table = _display_rich
    _display = display
except NameError:
    pass

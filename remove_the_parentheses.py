"""
This kata involves the removal of any occurrence of string sections between parentheses.

"""

import re

def remove_parentheses(st):
    """Function to remove any string sections enclosed in parenetheses 
    along with the parentheses
    
    arg: string
    returns: string without the unwanted sections
    """

    pattern = '\(([^)]+)\)'
    print(st)
    x = re.findall(pattern, st)
    
    for i in x:
        st = st.replace(f'({i})', '')
    
    return st.replace(')', '')

repr(remove_parentheses("example(unwanted thing)example"))

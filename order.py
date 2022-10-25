"""
    Finding the correct sequence of an order from a menu
"""


import re


def get_order(order):
    """function to get order from a menu
    Args:       order (str)
    Returns:    str (correct order)
    """
    
    menu_pattern = 'Burger|Fries|Chicken|Pizza|Sandwich|Onionrings|Milkshake|Coke'
    menu_list = menu_pattern.split('|')

    retrieved_order = re.findall(menu_pattern, order, re.IGNORECASE)
    retrieved_order = [i.title() for i in retrieved_order]

    res = {}
    for i in retrieved_order:
        res[i] = retrieved_order.count(i)

    output = ''
    for i in menu_list:
        if i in res.keys():
            output += (i + ' ') * res[i]
    return output.rstrip()


def get_order2(order):
    """function to get order from a menu
    Args:       order (str)
    Returns:    str (correct order)
    """
    
    menu = ['burger','fries','chicken','pizza','sandwich','onionrings','milkshake','coke']
    clean_order = ""
    for i in menu:
        clean_order += (i.capitalize() + ' ') * order.count(i)
    return clean_order.rstrip()



test1 = print(get_order('milkshakeonionringsburgerfriesburger'))
test2 = print(get_order2('milkshakeonionringsburgerfriesburger'))

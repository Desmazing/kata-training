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
    

print(get_order('milkshakeonionringsburgerfries'))

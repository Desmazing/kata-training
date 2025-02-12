""" 
Each hombre in the squad is to paint just one letter
Determine the frequency of each letter being painted between a range of numbers
"""


def paint_letterboxes(start, finish):
    """Function to determine how many times each no. box is painted in sequence
    Args:   int > starting number; int > finishing number
    Returns: list of ints > frequency of painting per number
    """
    mylist = list(range(start, finish))
    myotherlist = list(map(str, mylist))
    print(myotherlist)


paint_letterboxes(132, 137)

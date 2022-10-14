"""
    Determine how many key presses a user has to do to write a phrase
    on an old mobile phone keypad as below:

    -------------------------------------
    |     1     |   ABC 2   |   DEF 3   |
    -------------------------------------
    |   GHI 4   |   JKL 5   |   MNO 6   |
    -------------------------------------
    |   PQRS 7  |   TUV 8   |   WXYZ 9  |
    -------------------------------------
    |     *     |    0  _   |      #    |
    -------------------------------------
    
    Smart phones saved the world

"""


def presses(phrase):
    """function to determine number of presses a user does to write a phrase
        on an old mobile phone

    Args:       str - phrase to be typed out.
    Returns:    int - no. of presses undertaken.
    """

    press_dict = {'A':1,'B':2,'C':3,'D':1,'E':2,'F':3,'G':1,'H':2,'I':3,
                 'J':1,'K':2,'L':3,'M':1,'N':2,'O':3,'P':1,'Q':2,
                 'R':3,'S':4,'T':1,'U':2,'V':3,'W':1,'X':2,'Y':3,'Z':4, ' ':1,
                 '0':2,'1':1,'2':4,'3':4,'4':4,'5':4,'6':4,'7':5,'8':4,'9':5,
                 '*':1,'#':1}
    
    return f"{sum(press_dict[i.upper()] for i in phrase)} presses"


test1 = print(presses('HOW R U'))   # should return '13 presses'.
test2 = print(presses('LOL'))       # should return '9 presses'.

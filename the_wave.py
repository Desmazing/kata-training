"""
Recreation of the Mexican Wave using strings
- Lowercase letters simulate people sat down
- Uppercase letters simulate people standing up
- Spaces simulate empty seats
"""


def wave(people):
    """
    Function to simulate The Mexican Wave
    args:       String(lowercase) > to represent people seated in a stadium
    returns:    List > to simulate the wave
    """

    # str1 = ''
    lst1 = []
    for index, letter in enumerate(people):
        print(index, letter)
        lst1.append(people[index].replace(people[index], people[index].upper()))
        continue

    print(lst1)
wave("hello")

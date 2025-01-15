"""
Recreation of the Mexican Wave using strings
- Lowercase letters simulate people sat down
- Uppercase letters simulate people standing up
- Spaces simulate empty seats
Implemented using string slicing for ideal results
"""


def wave(people):
    """
    Function to simulate The Mexican Wave
    args:       String(lowercase) > to represent people seated in a stadium
    returns:    List > to simulate the wave
    """

    my_string = ''
    my_list = []
    for index, letter in enumerate(people):
        if letter.isalpha():
            my_string = people[:index] + people[index].upper() + people[index+1:]
            my_list.append(my_string)
        continue
    return my_list


def wave_version_2(people):
    """
    Function to simulate The Mexican Wave
    args:       String(lowercase) > to represent people seated in a stadium
    returns:    List > to simulate the wave
    """
    return [people[:index] + people[index].upper() + people[index+1:] \
            for index, letter in enumerate(people) if letter.isalpha()]


print(repr(wave("hello")))
print(repr(wave("two words")))

print(repr(wave_version_2("hello")))
print(repr(wave_version_2("two words")))

def solve(s):
    """Function to find the value of the longest consonant substring
    Args:       
            s (string)
    Returns:    
            int (consonant value)
    """
    max_ord = 0
    curr_ord = 0
    
    for i in s:
        if i not in 'aeiou':
            curr_ord += ord(i) - 96
        else:
            if curr_ord > max_ord:
                max_ord = curr_ord
            curr_ord = 0
    return max_ord


test1 = print(solve('zodiac'))
test2 = print(solve('strength'))
test3 = print(solve('catchphrase'))

def longest(a1, a2):
    output = ''
    for i in a1:
        if i not in output: output += i
    for j in a2:
        if j not in output: output += j
    return ''.join(sorted(output))


test1 = print(longest("aretheyhere", "yestheyarehere"))
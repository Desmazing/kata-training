def longest(a1, a2):
    output = ''
    for i in a1:
        if i not in output: output += i
    for j in a2:
        if j not in output: output += j
    return ''.join(sorted(output))


def longest2(a1, a2):
    return ''.join(sorted(set(a1 + a2)))


a1 = "aretheyhere"
a2 = "yestheyarehere"

test1 = print(longest(a1, a2))
test2 = print(longest2(a1, a2))

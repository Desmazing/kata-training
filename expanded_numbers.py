def expanded_form(num):
    final = []
    res = list((str(num)[::-1]))
    for j in range(0, len(res)):
        res[j] = int(res[j]) * (10 ** j)
        if res[j] != 0:
            final.append(str(res[j]))
    return ' + '.join(reversed(final))


def expanded_form2(num):
    final = []
    res = list((str(num)[::-1]))
    for i,j in enumerate(res):
        if j != '0':
            final.append(str(int(j) * (10 ** i)))
    return ' + '.join(reversed(final))


test1 = print(expanded_form(4982042))
test2 = print(expanded_form2(209))

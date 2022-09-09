def expanded_form(num):
    res = []
    final = []
    a = list(str(num)[::-1])
    for i in a:
        res.append(int(i))
    for j in range(0, len(res)):
        res[j] = res[j] * (10 ** j)
        if res[j] != 0:
            final.append(str(res[j]))
    return ' + '.join(reversed(final))


test1 = print(expanded_form(4982042))
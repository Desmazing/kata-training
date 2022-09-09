def expanded_form(num):
    res = []
    final = []
    res = list((str(num)[::-1]))
    for j in range(0, len(res)):
        res[j] = int(res[j]) * (10 ** j)
        if res[j] != 0:
            final.append(str(res[j]))
    return ' + '.join(reversed(final))


test1 = print(expanded_form(4982042))
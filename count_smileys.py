# count number of smiles in an arr


import re


def count_smileys(arr):
    smiley = re.compile(r"[:;][-~]?[)D]")
    return sum(bool(re.match(smiley, i)) for i in arr)


test1 = print(count_smileys([':D',':~)',';~D',':)']))
test2 = print(count_smileys([':)',':(',':D',':O',':;']))
test3 = print(count_smileys([';]', ':[', ';*', ':$', ';-D']))

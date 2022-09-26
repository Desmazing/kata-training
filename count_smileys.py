# count number of smiles in an arr


import re


def count_smileys(arr):
    smiley = re.compile(r"[:;][-~]?[)D]")
    return sum(bool(re.match(smiley, i)) for i in arr)


# def count_smileys2(arr):
#     return sum(1 for i in arr if re.match(r'\A[:;][-~]?[)D]Z\', i))

test1 = print(count_smileys([':D',':~)',';~D',':)']))
test2 = print(count_smileys([':)',':(',':D',':O',':;']))
test3 = print(count_smileys([';]', ':[', ';*', ':$', ';-D']))

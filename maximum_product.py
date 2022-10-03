#  find the maximum product of adjacent elements in an array
#  the second solution uses the zip function


def max_product(arr):
    lst = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j-1]:
                lst.append(arr[i] * arr[j])
                break
    return max(lst)


def max_product2(arr):
    """refactored using zip function solution inspired by one-liner return statements"""
    return max([a * b for a,b in zip(arr, arr[1:])])


test1 = print(max_product([5, 8])) # 40
test2 = print(max_product([1, 2, 3])) # 6
test3 = print(max_product([1, 5, 10, 9])) # 90
test4 = print(max_product([5, 1, 2, 3, 1, 4])) # 6
test5 = print(max_product2([-23, 4, -5, 99, -27, 329, -2, 7, -921])) # -14
test6 = print(max_product2([5, 1, 1, 8])) # 8

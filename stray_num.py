def stray(arr):
    return min(arr, key=arr.count)


test1 = print(stray([1,1,1,1,4,1,1]))

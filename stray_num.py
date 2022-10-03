def stray(arr):
    """min function takes 2 arguments the latter optional but powerful"""
    return min(arr, key=arr.count)


test1 = print(stray([1,1,1,1,4,1,1]))

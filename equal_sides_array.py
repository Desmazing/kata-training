# You are going to be given an array of integers. 
# Your job is to take that array and find an index N where the sum of the integers 
# to the left of N is equal to the sum of the
# integers to the right of N. If there is no index that would make this happen, return -1.


def equal_sides(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1


arr1 = [1,2,3,4,3,2,1]
arr2 =[1,100,50,-51,1,1]

test1 = print(equal_sides(arr1))
test2 = print(equal_sides(arr2))

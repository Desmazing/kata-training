# this is incomplete.

def two_sum(numbers, target):
    
    output = []
    for i in numbers:
        for j in numbers:
            if i + j == target and i != j:
                output.append(numbers.index(i))
                if numbers.index(j) not in output:
                    output.append(numbers.index(j))
    return output


test1 = print(two_sum([1,2,3], 4))

def solution(array_a, array_b):
    means = []
    for i in range(0,len(array_a)):
        diff_sq = (array_a[i] - array_b[i]) ** 2
        means.append(diff_sq)
    avg = sum(means) / len(means)
    return avg

print(solution([1,2,3], [4,5,6]))
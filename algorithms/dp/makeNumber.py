def makeNumber(n, m):
    sum_N = [1]
    for i in range(1, min(n, m) + 1): # min(n, m)은 m > n인 경우를 고려
        sum_temp += makeNumber(n-i, m)
    sum_N.append(sum_temp)
    return sum_N
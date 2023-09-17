def solution(n):
    count = 0
    num = []
    for i in range(4, n+1):
        for j in range(1, i+1):
            if i % j == 0:
                num.append(i)
        if num.count(i) >= 3:
            count += 1
    return count
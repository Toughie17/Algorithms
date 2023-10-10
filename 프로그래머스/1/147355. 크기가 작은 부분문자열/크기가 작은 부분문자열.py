def solution(t, p):
    count = 0
    leng = len(p)
    
    for i in range(len(t) - leng + 1):
        num = t[i: i + leng]
        if int(num) <= int(p):
            count += 1
    
    return count
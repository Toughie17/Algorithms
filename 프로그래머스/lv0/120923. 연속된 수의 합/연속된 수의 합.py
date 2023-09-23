def solution(num, total):
    #가우스 공식
    #연속합 = n / 2 (2 * 첫 수 + (n - 1)d) 
    result = []
    a = (2 * total / num - (num - 1)) / 2
    
    for i in range(num):
        result.append(a + i)
    return result
    
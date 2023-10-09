def solution(n):
    result = ''
    
    while n > 0:
        n, remainder = divmod(n, 3)
        result = str(remainder) + result
    print(result)
    answer = result[::-1]
    print(answer)
    
    return int(answer,3)
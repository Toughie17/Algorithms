def solution(n):
    result = 0
    #홀수인 경우
    if n % 2 == 1:
        for i in range(n+1):
            if i % 2 == 1:
                result += i             
    else:
        for i in range(n+1):
            if i % 2 == 0:
                result += i * i

    return result
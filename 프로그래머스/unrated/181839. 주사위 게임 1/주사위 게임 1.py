def solution(a, b):
    
    if a % 2 == 1 and b % 2 == 1:
        return a*a + b*b
    elif a % 2 == 0 and b % 2 == 0:
        return abs(a-b)
    else:
        return 2 * (a + b)
    
    # 삼항 연산자를 쓰는 경우
    # return a * a + b * b if a % 2 ==1 and b % 2 == 1 else abs(a - b) if a % 2 == 0 and b % 2 == 0 else 2 * (a + b)
def solution(n):
    sqr = int(n ** 0.5)
    
    if sqr * sqr == n:
        return 1
    return 2
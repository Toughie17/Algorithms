def solution(n):
#     sqr = int(n ** 0.5)
    
#     if sqr * sqr == n:
#         return 1
#     return 2
    #정수인지 판별. is_integer()
    return 1 if (n ** 0.5).is_integer() else 2
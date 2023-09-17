# def solution(n):
#     sol = 1
    
#     while True:
#         result = 1
        
#         for i in range(1, sol + 1):
#             result *= i
            
#         if result > n:
#             return sol - 1
#         else:
#             sol += 1

from math import factorial
    
def solution(n):
    k = 10
    while n < factorial(k):
        k -= 1
    return k
        
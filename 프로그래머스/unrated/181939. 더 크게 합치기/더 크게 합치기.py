def solution(a, b):
#     left = int(str(a) + str(b))
#     right = int(str(b) + str(a))
    
#     if left > right:
#         return left
#     elif right > left:
#         return right
#     else:
#         return left
    
    #다른 풀이
    return max(map(int,(f"{a}{b}", f"{b}{a}")))
    
def solution(dot):
#     # [양수/음수]
#     x = dot[0]
#     y = dot[1]
    
#     if x > 0 and y >0:
#         return 1
#     elif x < 0 and y > 0:
#         return 2
#     elif x < 0 and y < 0:
#         return 3
#     elif x > 0 and y < 0:
#         return 4
    
    
    x, y = dot
    
    if x * y > 0:
        return 1 if x > 0 else 3
    if x * y < 0:
        return 2 if x < 0 else 4
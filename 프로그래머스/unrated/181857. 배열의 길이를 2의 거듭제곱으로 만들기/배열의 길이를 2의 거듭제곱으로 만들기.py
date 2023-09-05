def solution(arr):
#     current = len(arr)
#     two = 1
    
#     while two < current:
#         two *= 2
    
#     if current != two:
#         while len(arr) < two:
#             arr.append(0)
            
#     return arr
    current = len(arr)
    num = 1
    
    while num < current:
        num *= 2
        
    # return arr + ([0] * (num - current))
    arr.extend([0] * (num - current))
    return arr
    #extend는 return값이 없다! 
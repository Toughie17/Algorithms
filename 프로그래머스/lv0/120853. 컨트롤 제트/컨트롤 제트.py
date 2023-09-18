def solution(s):
#     eles = s.split()
#     result = 0
    
#     for index, ele in enumerate(eles):
#         if ele == 'Z':
#             prev = int(eles[index - 1])
#             result -= prev
#         else:
#             result += int(eles[index])
            
#     return result

    #스택 활용
    stack = []
    for ele in s.split():
        if ele != 'Z':
            stack.append(int(ele))
        else:
            stack.pop()
            
    return sum(stack)
    
    
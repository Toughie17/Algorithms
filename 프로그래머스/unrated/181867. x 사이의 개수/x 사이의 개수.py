def solution(myString):
#     result = []
    
#     for x in myString.split('x'):
#         result.append(len(x))
#     return result

    return [len(x) for x in myString.split('x')]
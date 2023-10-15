def solution(array, commands):

#     answer = []

#     for com in commands:
#         part = array[com[0] - 1: com[1]]
#         answer.append(sorted(part)[com[2] - 1])
    
#     return answer

    return [sorted(array[com[0] -1: com[1]])[com[2]-1] for com in commands]
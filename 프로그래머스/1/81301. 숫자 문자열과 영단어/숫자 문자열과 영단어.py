def solution(s):
#     table = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
#             'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    
#     answer = []
#     temp = ''

#     for cha in s:
#         if cha.isdigit():
#             answer.append((cha))
#         else:
#             temp += cha
#             if temp in table:
#                 answer.append(str((table[temp])))
#                 temp = ''
    
#     return(int(''.join(answer)))

    table = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for i in range(len(table)):
        s = s.replace(table[i], str(i))
    return int(s)
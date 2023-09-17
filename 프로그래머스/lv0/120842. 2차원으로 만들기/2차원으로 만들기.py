def solution(num_list, n):
#     row = len(num_list) // n
#     answer = []
#     for i in range(row):
#         temp = []
#         for num in num_list:
#             if len(temp) < n:
#                 temp.append(num)
#         answer.append(temp)
#         num_list  = num_list[n:]
        
#     return answer
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])
    return answer
        
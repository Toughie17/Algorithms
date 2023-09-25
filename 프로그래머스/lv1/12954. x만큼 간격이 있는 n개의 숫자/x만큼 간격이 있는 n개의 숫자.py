def solution(x, n):
#     answer = []
#     start = x
    
#     while len(answer) < n:
#         answer.append(start)
#         start += x
#     return answer

    return [x * i for i in range(1, n + 1)]
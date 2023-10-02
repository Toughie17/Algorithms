def solution(n):
#     answer = []
    
#     for i in range(1, n + 1):
#         #홀수면 수 짝수면 박
#         if i % 2 == 1:
#             answer.append('수')
#         else:
#             answer.append('박')
            
#     return ''.join(answer)

    return '수박' * (n // 2) + '수' * (n % 2)
        
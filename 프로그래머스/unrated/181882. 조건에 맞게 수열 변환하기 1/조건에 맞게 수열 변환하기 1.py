def solution(arr):
#     answer = arr
    
#     for index in range(len(arr)):
#         if answer[index] >= 50 and answer[index] % 2 == 0:
#             answer[index] /= 2
#         elif answer[index] < 50 and answer[index] % 2 == 1:
#             answer[index] *= 2
            
#     return answer
#위는 처음 작성 코드
    answer = arr.copy()
    for index, value in enumerate(answer):
        if value >= 50 and value % 2 == 0:
            answer[index] /= 2
        elif value < 50 and value % 2 == 1:
            answer[index] *= 2
    return answer
#enumerate 사용한 방법

def solution(absolutes, signs):
    answer = 0
    
#     for i, num in enumerate(absolutes):
#         if signs[i]:
#             answer += num
#         else:
#             answer -= num
#     return answer

    for num, sign in zip(absolutes, signs):
        if sign:
            answer += num
        else:
            answer -= num
    return answer
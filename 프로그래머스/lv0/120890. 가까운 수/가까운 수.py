def solution(array, n):

#     closest_num = array[0]
#     current_diff = abs(array[0] - n)
    
#     for num in array:
#         diff = abs(num - n)
#         if diff < current_diff or (diff == current_diff and num < closest_num):
#             closest_num = num
#             current_diff = diff
            
#     return closest_num
    
    # sort- key 활용
    answer = sorted(array, key = lambda x: (abs(x - n), x - n))
    return answer[0]
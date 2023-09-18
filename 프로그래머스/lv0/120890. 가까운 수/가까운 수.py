def solution(array, n):
#     check = []
#     for index, num in enumerate(array):
#         check.append((abs(num - n), index, num))
    
#     # 가장 가까운 수가 여러 개일 경우 더 작은 수를 return 합니다.
#     minimum = min(check)[0]
    
#     if check.count(minimum) >= 2:
#         pass
#     else:
#         return array[min(check)[1]]

    closest_num = array[0]
    current_diff = abs(array[0] - n)
    
    for num in array:
        diff = abs(num - n)
        if diff < current_diff or (diff == current_diff and num < closest_num):
            closest_num = num
            current_diff = diff
            
    return closest_num
def solution(num_list):
#     last_value = num_list[-1]
#     before_value = num_list[-2]
    
#     if last_value > before_value:
#         num_list.append(last_value - before_value)
#     else:
#         num_list.append(last_value * 2)
    
#     return num_list

# 배열 슬라이싱 활용

 #조건문 활용 더 짧은 답안
    # .append(넣을 요소, 조건문, 아닌 경우 넣을 요소)
    num_list.append((num_list[-1] - num_list[-2]) if num_list[-1] > num_list[-2] else num_list[-1] * 2 )
    
    return num_list
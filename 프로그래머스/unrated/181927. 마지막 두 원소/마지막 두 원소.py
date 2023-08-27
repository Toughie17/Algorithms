def solution(num_list):
    last_value = num_list[-1]
    before_value = num_list[-2]
    
    if last_value > before_value:
        num_list.append(last_value - before_value)
    else:
        num_list.append(last_value * 2)
    
    return num_list

# 배열 슬라이싱 활용
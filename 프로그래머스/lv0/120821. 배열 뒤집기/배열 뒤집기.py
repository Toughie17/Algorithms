def solution(num_list):
    # return sorted(num_list, reverse = True) # 실패. 정렬이 아니라 뒤집기만 하도록
    # return num_list[::-1]
    
    # reverse 사용
    return list(reversed(num_list))
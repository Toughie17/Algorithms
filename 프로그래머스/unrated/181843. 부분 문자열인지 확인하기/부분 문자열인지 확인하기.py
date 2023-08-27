def solution(my_string, target):
    # return int(target in my_string)

    # 만약 in 안쓴다면
    # 앞에서부터 찾아본다.
    target_len = len(target)
    my_string_len = len(my_string)
    
    for i in range(my_string_len - target_len + 1):
        if my_string[i: i + target_len] == target:
            return 1
    return 0
def solution(array):
    cnt = {}
    
    for num in array:
        if num in cnt:
            cnt[num] += 1
        else:
            cnt[num] = 1
            
    max_cnt = 0
    mode = -1
    
    for num, count in cnt.items():
        if count > max_cnt:
            max_cnt = count
            mode = num
        elif count == max_cnt:
            mode = -1
            
    return mode
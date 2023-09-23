def solution(array):
    cnt = {}
    
    for num in array:
        if num in cnt:
            cnt[num] += 1
        else:
            cnt[num] = 1
    
    
    max_count = 0
    mode = -1
    
    for num, count in cnt.items():
        if count > max_count:
            max_count = count
            mode = num
        elif max_count == count:
            mode = -1
            
    return mode

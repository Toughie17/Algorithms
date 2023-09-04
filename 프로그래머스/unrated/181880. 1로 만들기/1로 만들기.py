def solution(num_list):
    count = 0
    
    for num in num_list:
        one = num
        while one > 1:
            if one % 2 == 0:
                one //= 2
                count += 1
            else:
                one = (one-1) // 2
                count += 1
                
    return count

            
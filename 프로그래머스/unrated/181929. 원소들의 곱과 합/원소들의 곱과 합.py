def solution(num_list):
    multiple = 1
    sum = 0
    
    for num in num_list:
        multiple *= num
        sum += num
    
    if multiple < sum * sum:
        return 1

    return 0
def solution(array):
    count = 0
    
    for num in array:
        for ele in str(num):
            if ele == '7':
                count += 1
    return count
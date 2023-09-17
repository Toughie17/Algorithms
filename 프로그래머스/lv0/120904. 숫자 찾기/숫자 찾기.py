def solution(num, k):
    
    for index, number in enumerate(str(num)):
        if number == str(k):
            return index + 1
    
    return -1
        
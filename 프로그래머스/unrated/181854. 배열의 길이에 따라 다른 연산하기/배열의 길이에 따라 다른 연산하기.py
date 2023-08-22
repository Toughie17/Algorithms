def solution(arr, n):
    
    result = []
    
    if len(arr) % 2 == 1:
        for index, value in enumerate(arr):
            if index % 2 == 0:
                result.append(value + n)
            else:
                result.append(value)
        return result
    
    else:
        for index, value in enumerate(arr):
            if index % 2 == 1:
                result.append(value + n)
            else:
                result.append(value)
        return result
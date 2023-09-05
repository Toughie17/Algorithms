def solution(arr):
    indexs = []
    
    for index, num in enumerate(arr):
        if num == 2:
            indexs.append(index)
    if indexs:
        return arr[indexs[0] : indexs.pop() + 1]
    
    return [-1]
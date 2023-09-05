def solution(arr):
    indexs = []
    
    for index, num in enumerate(arr):
        if num == 2:
            indexs.append(index)
    if indexs:
        return arr[indexs[0] : indexs.pop() + 1]
    return [ -1]
    
    # return [-1] if 2 not in arr else arr[arr.index(2): len(arr) - arr[::-1].index(2) ]


def solution(arr, flag):
    result = []
    
    for i in range(len(flag)):
        if flag[i]:
            result.extend([arr[i]] * (arr[i] *2))
        else:
            # for i in range(arr[i]):
            #     result.pop()
            result = result[:-arr[i]]
                
    return result
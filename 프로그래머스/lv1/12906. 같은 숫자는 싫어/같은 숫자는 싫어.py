def solution(arr):
    result = []
    
    # for num in arr:
    #     if result[-1:] == [num]:
    #         continue
    #     else:
    #         result.append(num)
    
    for i in range(len(arr)):
        if i == 0:
            result.append(arr[i])
        elif arr[i - 1] != arr[i]:
            result.append(arr[i])
                
    return result
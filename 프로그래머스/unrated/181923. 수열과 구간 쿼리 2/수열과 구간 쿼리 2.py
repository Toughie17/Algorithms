def solution(arr, queries):
    result = []
    
    for (s, e, k) in queries:
        find = []
        
        for i in range(s, e + 1):
            if arr[i] > k:
                find.append(arr[i])
        result.append(min(find) if find else -1)
        
    return result
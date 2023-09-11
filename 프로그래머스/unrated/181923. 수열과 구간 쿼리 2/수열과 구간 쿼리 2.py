def solution(arr, queries):
    answer = []
    
    for (s, e, k) in queries:
        lowest = []
        
        for i in range(s,e + 1):
            if arr[i] > k:
                lowest.append(arr[i])
                
        if lowest:
            answer.append(min(lowest))
        else:
            answer.append(-1)
            
    return answer

        
        
def solution(arr, queries):
    result = arr.copy()
    
    for query in queries:
        for j in range(query[0], query[1]+1):
            result[j] += 1
            
    return result
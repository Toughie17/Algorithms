def solution(arr, queries):
    
    for query in queries:
        for i in range(query[0], query[1] + 1):
            #i가 k의 배수이면
            if i % query[2] == 0:
                arr[i] += 1
    return arr
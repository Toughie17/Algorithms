import numpy as np
def solution(arr1, arr2):
    result = []
    
    row = len(arr1)
    col = len(arr1[0])
    
    for i in range(row):
        new = []
        for j in range(col):
            new.append(arr1[i][j] + arr2[i][j])
        result.append(new)
    return result

    #ZIP 쓰는 방법
    # answer = [[c + d for c, d in zip(a,b)] for a, b in zip(A,B)]
    # a, b = ([1,2], [3, 4]) , ([2,3], [5,6])
    # c, d = ([1,2], [2, 3]) , ([3,4], [5,6])
    
    # return answer
    
    #넘파이 쓰는 방법
    # A_np = np.array(arr1)
    # print(A_np)
    # B_np = np.array(arr2)
    # print(B_np)
    # result = A_np + B_np
    # print(result)
    # print(result.tolist())
    # return result.tolist()
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
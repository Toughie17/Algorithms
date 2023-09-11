def solution(arr):
    
    row_len = len(arr)
    col_len = len(arr[0])
    
    if row_len > col_len:
        for i in range(len(arr)):
            arr[i].extend([0] * (row_len - col_len))
    elif row_len < col_len:
        for _ in range(col_len - row_len):
            arr.append([0] * col_len)
    
    return arr

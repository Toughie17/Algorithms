# def solution(arr):
#     row_len = len(arr)
#     col_len = len(arr[0])
    
#     if row_len > col_len:
#         for i in range(len(arr)):
#             arr[i].append(0 * (col_len - row_len))
    
#     elif col_len > row_len:
#         for _ in range(col_len - row_len):
#             arr.append([0] * (col_len))
    
#     return arr

# def solution(arr):
#     answer = []
    
#     row = len(arr)
#     col = len(arr[0])
    
#     if row > col:
#         for i in arr:
#             answer.append(i + [0] * (row - col))
#     elif row < col:
#         for _ in range(col - row):
#             arr.append([0] * col)
#         answer = arr
#     else:
#         answer = arr
    
#     return answer

def solution(arr):
    num_rows = len(arr)
    num_cols = len(arr[0])

    if num_rows > num_cols:
        for i in range(num_rows):
            arr[i] += [0] * (num_rows - num_cols)
    elif num_cols > num_rows:
        for i in range(num_cols - num_rows):
            arr.append([0] * num_cols)

    return arr
def solution(board, k):
    row = len(board)
    col = len(board[0])
    result = 0
    
    for i in range(row):
        for j in range(col):
            if i + j <= k:
                result += board[i][j]
    return result
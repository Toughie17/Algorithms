def solution(board):
    n = len(board)
    danger = set()
    
    for i, row in enumerate(board):
        #3, [0,0,1,0,0]
        for j, x in enumerate(row):
            #2, 1
            if x:
                danger.update(
                    (i + di, j + dj)
                    #위의 행, 자기 행, 아래 행
                    for di in [-1, 0, 1]
                    #각 행에서 왼쪽, 지뢰위치, 오른쪽
                    for dj in [-1, 0, 1]
                    if 0 <= i + di < n and 0 <= j + dj < n
                )
    
    return n * n - len(danger)

# [0,0,0,0,0]
# [0,0,0,0,0]
# [0,x,x,x,0]
# [0,x,1,x,0]
# [0,x,x,x,0]
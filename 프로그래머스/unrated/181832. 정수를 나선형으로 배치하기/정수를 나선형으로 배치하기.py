def solution(n):
    dr = 0
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    
    arr = [[0] * n for _ in range(n)]
    
    i, j, cnt = 0, 0, 1
    
    arr[i][j] = cnt
    
    while cnt < n * n:
        ni, nj = i + di[dr], j + dj[dr]
        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 0:
            i, j = ni, nj
            cnt += 1
            arr[i][j] = cnt
        else:
            dr = (dr + 1) % 4
        
    return arr
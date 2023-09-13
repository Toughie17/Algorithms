def solution(n):
    # 채울 칸
    arr = [[0] * n for _ in range(n)]
    # 좌표, 채울 숫자
    i, j, cnt = 0, 0, 1
    # 방향
    dr = 0
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    
    #첫번째 칸을 채워주자.
    arr[i][j] = cnt
    cnt += 1
    #cnt가 n*n이 될 때까지 반복함.
    while cnt <= n * n:
        # 이동 준비를 한다.
        ni, nj = i + di[dr], j + dj[dr]
        # 이동 할 위치가 범위 내이고 다음 값이 0인지 확인한다.
        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 0:
            #조건을 다 만족했으니 이동 후 증가시킨 값을 넣어준다.
            i, j = ni, nj
            arr[i][j] = cnt
            cnt += 1
        else:
            #방향 전환을 해준다. (범위를 벗어나거나, 다음 자리에 값이 있는 경우니)
            dr = (dr + 1) % 4
            # index out of range 방지: 4로 나눈 나머지를 할당(0,1,2,3)
    
    return arr
            
            
            
            
            
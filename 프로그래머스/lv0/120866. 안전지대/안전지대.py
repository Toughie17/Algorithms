def solution(board):
    #전체 칸 수에서 위험지역 칸 수를 빼서 답을 구한다.
    n = len(board)
    #지뢰가 인접한 경우 중복되는 위험 지역이 있기 때문에 set 활용
    danger = set()
    
    #먼저 행을 순회하고
    for i, row in enumerate(board):
        #열을 순회하면서 1을 찾는다.
        for j, x in enumerate(row):
            # 1을 찾자(지뢰 찾기) - 정수의 경우 0이 False 이외는 1임을 활용 
            if x:
                danger.update(
                    #몇행 몇열? 
                    (i + di, j + dj)
                    #위 아래 행 + 지뢰자리
                    for di in [-1, 0, 1]
                    #양 옆 열 + 지뢰자리
                    for dj in [-1, 0, 1]
                    #보드를 벗어나지 않는 경우만
                    if 0<= i + di < n and 0 <= j + dj < n
                )
                
    return n * n - len(danger)
            
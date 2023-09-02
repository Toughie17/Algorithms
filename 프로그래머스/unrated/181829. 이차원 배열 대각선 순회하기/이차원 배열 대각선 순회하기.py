def solution(board, k):
    row = len(board)
    col = len(board[0])
    result = 0
    
    for i in range(row):
        for j in range(col):
            if i + j <= k:
                result += board[i][j]
    return result

    '''
    자꾸 런타임 에러가 났는데, 배열 out of range 문제 같음.
    n * n 배열로 단순히 생각했는데,
    2차월의 배열의 경우 행과 열의 개수가 다를 수 있음 (ex. 3 * 4 배열)
    따라서 행의 길이를 구하고 (board의 길이)
    열의 길이를 따로 구하고(열의 길이는 첫 행의 요소 개수일 것이니)
    행, 열 길이마다 반복문을 돌아주면 되는 것
    ''' 
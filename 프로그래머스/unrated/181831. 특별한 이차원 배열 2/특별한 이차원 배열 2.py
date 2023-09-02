def solution(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            #모두 대칭인 것을 확인해야함.
            # 여기서 대칭인 것을 만날 때 바로 1을 return하면 배열을 전부 순회하지 못함.
            # 따라서 배열을 전부 순회하기 위해 배열이 대칭이 아닌 지점을 찾는 코드
            if arr[i][j] != arr[j][i]:
                return 0
    return 1
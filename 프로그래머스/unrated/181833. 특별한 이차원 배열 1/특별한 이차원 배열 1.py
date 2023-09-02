def solution(n):
    arr = []
    
    for i in range(n):
        #행 만들기
        row = []
        for j in range(n):
            #열 만들기
            if i == j:
                row.append(1)
            else:
                row.append(0)
        #열을 다 채우면 arr에 추가
        arr.append(row)
        
    return arr
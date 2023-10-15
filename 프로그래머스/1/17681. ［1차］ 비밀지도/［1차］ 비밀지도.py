def solution(n, arr1, arr2):
    #일단 01001 이런 식으로 변환해야함. bin 활용
    #bin을 쓰면 앞에 0b가 붙어서 슬라이싱으로 제거해준다.
    map1 = [bin(num)[2:] for num in arr1]
    #열의 길이가 n과 같아야함. 그래서 앞에 모자란 만큼 0을 붙여줘야함.
    map1 = ['0' * (n- len(num)) + num for num in map1]
    
    #map2도 똑같이 해준다.
    map2 = [bin(num)[2:] for num in arr2]
    map2 = ['0' * (n- len(num)) + num for num in map2]
    
    answer = []
    #행 열
    for row_idx in range(n):
        line = ''
        for col_idx in range(n):
            #지도 1과 지도 2의 행, 열 확인해보기. 1이야 0이야
            # 둘 다 0이어야 공백을 추가해야함.
            if map1[row_idx][col_idx] == '0' and map2[row_idx][col_idx] == '0':
                line += ' '
            #지도 1과 지도 2 중에 한 곳이라도 1이 있으면 #을 붙여줘야함.
            else:
                line += '#'
        answer.append(line)
        
    return(answer)
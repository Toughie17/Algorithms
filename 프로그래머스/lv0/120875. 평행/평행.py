def solution(dots):
    # 어떤 경우가 평행일까?
    #  1사분면만 생각하면 됨
    # 기울기
    
    #점을 x축 기준으로 오름차순 정렬하고
    # 가로로 그어보고 세로로 그어보고
    # 기울기가 같다면 평행하는 것으로.
    
    arr = sorted(dots)
    #세로로 그어보기
    left_incl =  (arr[1][1] - arr[0][1]) / (arr[1][0] - arr[0][0])
    right_incl = (arr[3][1] - arr[2][1]) / (arr[3][0] - arr[2][0])
    
    if left_incl == right_incl:
        return 1
    #가로로 그어보기
    upper_incl = (arr[3][1] - arr[1][1]) / (arr[3][0] - arr[1][0])
    down_incl = (arr[2][1] - arr[0][1]) / (arr[2][0] - arr[0][0])
    
    if upper_incl == down_incl:
        return 1
    
    return 0
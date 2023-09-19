def solution(sides):
    default = sorted(sides)[0]
    default_long = sorted(sides)[1]
    new_long = default_long + 1
    answer = []
    
    #가장 긴 변이 기본인 경우
    for i in range(1, default_long + 1):
        if default + i > default_long:
            answer.append(i)
    #가장 긴 변의 가능성
    while default + default_long > new_long:
        answer.append(new_long)
        new_long += 1
        
    return len(answer)
        
    
    # 짧은 변의 길이 * 2 -1
    # return (sorted(sides)[0] * 2) - 1
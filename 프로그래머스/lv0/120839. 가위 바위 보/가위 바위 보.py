def solution(rsp):
    answer = []
    
    #가위: 2, 바위:0, 보:5
    for enemy in rsp:
        if enemy == '2':
            answer.append(0)
        elif enemy == '0':
            answer.append(5)
        elif enemy == '5':
            answer.append(2)
            
    return ''.join(map(str,answer))
def solution(n, control):
    
    answer = n
    
    for con in control:
        if con == "w":
            answer += 1
        elif con == 's':
            answer -= 1
        elif con == 'd':
            answer += 10
        else:
            answer -= 10
            
    return answer
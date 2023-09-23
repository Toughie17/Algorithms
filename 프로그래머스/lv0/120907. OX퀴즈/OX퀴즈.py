def solution(quiz):
    answer = []
    
    # for q in quiz:
    #     splited = q.split(' = ')
    #     if eval(splited[0]) == int(splited[1]):
    #         answer.append('O')
    #     else:
    #         answer.append('X')
    # return answer

    for q in quiz:
        L,R = q.split(' = ')
        a,op,b = L.split()
        
        if op == '+':
            answer.append('O') if int(a) + int(b) == int(R) else answer.append('X')
        else:
            answer.append('O') if int(a) - int(b) == int(R) else answer.append('X')
    
    return answer
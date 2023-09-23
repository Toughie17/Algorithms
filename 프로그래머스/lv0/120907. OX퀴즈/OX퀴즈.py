def solution(quiz):
    answer = []
    
    for q in quiz:
        splited = q.split(' = ')
        if eval(splited[0]) == int(splited[1]):
            answer.append('O')
        else:
            answer.append('X')
    return answer
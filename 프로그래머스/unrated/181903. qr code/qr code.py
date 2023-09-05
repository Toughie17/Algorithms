def solution(q, r, code):
    answer = []
    for index, cha in enumerate(code):
        if index % q == r:
            answer.append(cha)
            
    return ''.join(answer)
def solution(x, n):
    answer = []
    start = x
    
    while len(answer) < n:
        answer.append(start)
        start += x
    return answer
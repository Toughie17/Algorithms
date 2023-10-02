def solution(n):
    answer = []
    
    for i in range(1, n + 1):
        #홀수면 수 짝수면 박
        if i % 2 == 1:
            answer.append('수')
        else:
            answer.append('박')
            
    return ''.join(answer)
        
def solution(emergency):
    answer = []
    
    temp = sorted(emergency, reverse = True)
    #[76, 24, 3]
    for num in emergency:
        answer.append(temp.index(num) + 1)
    return answer
def solution(score):
    average = [sum(i) / 2 for i in score]
    rank = sorted(average, reverse = True)
    
    answer = []
    for i in average:
        answer.append(rank.index(i) + 1)
    return answer
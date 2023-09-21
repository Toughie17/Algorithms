def solution(score):
    average = [sum(i) / len(i) for i in score]
    rank = sorted(average, reverse = True)
    
    return [rank.index(score) + 1 for score in average]
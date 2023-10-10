from itertools import combinations
def solution(number):
    result = 0
    for comb in combinations(number,3):
        if sum(comb) == 0 :
            result += 1
    
    return result
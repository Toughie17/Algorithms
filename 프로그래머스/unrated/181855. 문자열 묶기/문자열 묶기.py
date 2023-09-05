from collections import Counter

def solution(strArr):
    sol = []
    for str in strArr:
        sol.append(len(str))
        
    counts = Counter(sol)
    # Counter({길이1: 빈도수1, 길이2: 빈도수2, ...})
    
    return max(counts.values())
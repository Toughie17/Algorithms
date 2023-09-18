def solution(s):
    counts = {}
    
    for cha in s:
        if cha in counts:
            counts[cha] += 1
        else:
            counts[cha] = 1
    
    uniques = [cha for cha, count in counts.items() if count == 1]
    
    return ''.join(sorted(uniques))
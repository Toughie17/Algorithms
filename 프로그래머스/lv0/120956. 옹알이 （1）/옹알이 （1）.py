def solution(babbling):
    can = ["aya", "ye", "woo", "ma"]
    cnt = 0
    
    for babble in babbling:
        for speak in can:
            babble = babble.replace(speak,'*')
        
        if all(cha == '*' for cha in babble):
            cnt += 1
    return cnt
    
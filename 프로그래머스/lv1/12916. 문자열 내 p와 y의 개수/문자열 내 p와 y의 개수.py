def solution(s):
    s = s.lower()
    pcount = s.count('p')
    ycount = s.count('y')
    
    if pcount == ycount:
        return True
    elif pcount == 0 and ycount == 0:
        return True
    else:
        return False
    
    
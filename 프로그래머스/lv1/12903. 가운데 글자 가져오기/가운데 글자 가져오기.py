def solution(s):
    c = len(s) // 2
    
    if len(s) % 2 == 1:
        return s[c]
    else:
        return s[c-1: c + 1]
    
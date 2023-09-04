def solution(myString, pat):
    current = ''
    max = ''
    
    for cha in myString:
        current += cha
        if current.endswith(pat):
            max = current
            
    return max
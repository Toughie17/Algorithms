#ord, chr

def solution(s, n):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz" #26개 0~25번까지
    
    answer = []
    
    for cha in s:
        if cha.isupper():
            answer.append(upper[(upper.index(cha) + n) % 26])
        elif cha.islower():
            answer.append(lower[(lower.index(cha) + n) % 26])
        else:
            answer.append(' ')
            
    return ''.join(answer)
        
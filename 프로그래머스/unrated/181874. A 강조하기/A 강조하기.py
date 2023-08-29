def solution(myString):
    answer = ''
    
    for cha in myString:
        if cha == 'a':
            answer += "A"
        elif cha != "A" and cha.isupper():
                answer += cha.lower()
        else: answer += cha
                
    return answer
def solution(myString):
    #l보다 앞인지 뒤인지 어떻게 판단하지
    #문자열 직접 비교가 가능하네..
    result = ''
    
    for cha in myString:
        if cha < 'l':
            result += 'l'
        else:
            result += cha
            
    return result
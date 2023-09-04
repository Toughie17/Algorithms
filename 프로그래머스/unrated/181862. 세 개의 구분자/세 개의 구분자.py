def solution(myStr):
    result = []
    current = ''
    
    for cha in myStr:
        #구분자를 만났을 때
        if cha in 'abc':
            if current:
                result.append(current)
                current = ''
        else:
            current += cha
        
    if current:
        result.append(current)
        
    if result:
        return result
    else:
        return ["EMPTY"]
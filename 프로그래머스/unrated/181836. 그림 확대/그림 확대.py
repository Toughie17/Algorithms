def solution(picture, k):
    result = []
    
    for ele in picture:
        temp = []
        
        for cha in ele:
            if cha == '.':
                temp.append('.' * k)
            elif cha == 'x':
                temp.append('x' * k)
        for _ in range(k):
            result.append(''.join(temp))
            
    return result
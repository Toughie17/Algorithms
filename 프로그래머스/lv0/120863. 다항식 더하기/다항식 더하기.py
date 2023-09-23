def solution(polynomial):
    splited = polynomial.split(' + ')
    xnumber = 0
    const = 0
    
    for poly in splited:
        if poly == 'x':
            xnumber += 1
        elif poly.isdigit():
            const += int(poly)
        else:
            xnumber += int(poly[:-1])
    
    #상수항만 있는 경우
    if xnumber == 0:
        return str(const)
    #x의 계수가 1인 경우
    elif xnumber == 1:
        return f'x + {const}' if const != 0 else 'x'
    else:
        return f'{xnumber}x + {const}' if const != 0 else f'{xnumber}x'
    
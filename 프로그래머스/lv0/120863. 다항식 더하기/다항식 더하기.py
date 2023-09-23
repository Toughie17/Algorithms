def solution(polynomial):
    splited = polynomial.split(' + ')
    xnumber = 0
    number = 0
    
    for poly in splited:
        if poly == 'x':
            xnumber += 1
        elif len(poly) >= 2 and 'x' in poly:
            xnumber += int(poly[:-1])
        elif poly.isdigit():
            number += int(poly)
    
    #계수 1은 생략합니다.
    if xnumber == 1 and number:
        return f'x + {number}'
    elif xnumber == 1 and not number:
        return f'x'
    elif xnumber >= 2 and number:
        return f"{xnumber}x + {number}"
    elif xnumber >= 2 and not number:
        return f"{xnumber}x"
    elif number:
        return f'{number}'

    
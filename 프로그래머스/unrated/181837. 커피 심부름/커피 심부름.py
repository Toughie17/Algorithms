def solution(order):
    # 메뉴만 적은 팀원의 것은 차가운 것으로 통일
    # 아무거나는 차가운 아메리카노
    # 라떼 아니면 다 아아임
    aa = 0
    cl = 0
    
    for menu in order:
        if 'latte' in menu:
            cl += 5000
        else:
            aa += 4500
            
    return (aa + cl)
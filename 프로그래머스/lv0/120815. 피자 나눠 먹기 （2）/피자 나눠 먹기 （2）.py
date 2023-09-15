def solution(people):
    #총 피자 조각 수가 사람 수로 딱 나눠 떨어져야 한다.
    pizza = 1
    
    while (pizza * 6) % people != 0:
        pizza += 1
    return pizza
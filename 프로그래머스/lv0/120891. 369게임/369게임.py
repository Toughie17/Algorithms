def solution(order):
    sol = 0
    for num in str(order):
        if num in '369':
            sol+=1
    return sol
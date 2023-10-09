def solution(dept, budget):
    #많은 부서를 지원해주려면 지원금이 적은 부서들부터 지원해주면 됨
    #지원금이 큰 부서를 먼저 지원하면 예산을 많이 깎아먹기 때문
    
    dept = sorted(dept)
    count = 0
    
    for money in dept:
        if budget>= money:
            budget -= money
            count += 1
        else:
            continue
    return count
        
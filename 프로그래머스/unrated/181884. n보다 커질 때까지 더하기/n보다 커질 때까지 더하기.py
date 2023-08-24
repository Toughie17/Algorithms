def solution(numbers, n):
    total = 0
    
    for num in numbers:
        total += num
        if total > n:
            return total
    return total

#진짜 이상, 이하, 초과, 미만 조건 잘 보자..
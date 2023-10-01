def solution(numbers):
    # all = set(range(10))
    # return sum(all - set(numbers))

    return sum(num for num in list(range(10)) if num not in numbers)
    

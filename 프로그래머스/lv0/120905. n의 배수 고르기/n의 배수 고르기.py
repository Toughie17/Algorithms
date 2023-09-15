def solution(n, numlist):
    #n으로 나눠지는 애들만 담자
    return [num for num in numlist if num % n == 0]
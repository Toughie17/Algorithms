def solution(array, n):
    #반복문으로 바로 풀 수 있겠지만..
    
    sol = 0
    for num in array:
        if num == n:
            sol += 1
    return sol
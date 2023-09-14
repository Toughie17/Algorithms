def solution(s1, s2):
    sol = 0
    for num in s1:
        if num in s2:
            sol += 1
    return sol
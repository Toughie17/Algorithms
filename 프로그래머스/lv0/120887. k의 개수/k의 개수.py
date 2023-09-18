def solution(i, j, k):
    sol = 0
    
    for i in range(i, j + 1):
        for j in str(i):
            if j == str(k):
                sol += 1
                
    return sol
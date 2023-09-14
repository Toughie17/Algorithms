def solution(slice, n):
    sol = 1
    while slice * sol < n:
        sol += 1
    
    return sol
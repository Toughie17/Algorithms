def solution(slice, n):
#     sol = 1
#     while slice * sol < n:
#         sol += 1
    
#     return sol

    if n % slice == 0:
        return n // slice
    else:
        return n // slice + 1
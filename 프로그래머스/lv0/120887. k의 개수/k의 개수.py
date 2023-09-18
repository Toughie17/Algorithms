def solution(i, j, k):
#     sol = 0
    
#     for num in range(i, j + 1):
#         for j in str(num):
#             if j == str(k):
#                 sol += 1
                
#     return sol

    sol = 0
    
    for num in range(i, j + 1):
        sol += str(num).count(str(k))
    return sol
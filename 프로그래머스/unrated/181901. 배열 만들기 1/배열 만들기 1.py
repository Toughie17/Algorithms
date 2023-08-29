def solution(n, k):
#     result = []
    
#     for i in range(0,n+1,k):
#         if i != 0:
#             result.append(i)
            
#     return(result)

    return [ i for i in range(k,n+1,k)]
def solution(arr, query):
    
#     for i in range(len(query)):
#         if i % 2 == 0:
#             arr = arr[:query[i] + 1]
#         elif i % 2 == 1:
#             arr = arr[query[i]:]
            
#     return arr

    for (index, query) in enumerate(query):
        if index % 2 == 0:
            arr = arr[:query + 1]
        elif index % 2 == 1:
            arr = arr[query:]
    return arr
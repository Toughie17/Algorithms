def solution(todo_list, finished):
#     left = []
        
#     for index, todo in enumerate(todo_list):
#         if not finished[index]:
#             left.append(todo)
            
#     return left

    return [work for idx, work in enumerate(todo_list) if not finished[idx] ]
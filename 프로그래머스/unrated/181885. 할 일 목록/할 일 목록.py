def solution(todo_list, finished):
    left = []
        
    for index, todo in enumerate(todo_list):
        if not finished[index]:
            left.append(todo)
            
    return left
def solution(keyinput, board):
#     x = 0
#     y = 0
    
#     x_limit = (board[0] - 1) / 2
#     y_limit = (board[1] - 1) / 2
    
#     inputs = {'up': 1, 'down': -1, 'left': -1, 'right': 1}
    
#     for input in keyinput:
#         if input == 'up' or input == 'down':
#             new_y = y + inputs[input]
#             if -y_limit <= new_y <= y_limit:
#                 y = new_y
                
#         elif input == 'left' or input == 'right':
#             new_x = x + inputs[input]
#             if -x_limit <= new_x <= x_limit:
#                 x = new_x
    
#     return [x, y]
    x,y = 0,0
    xlim,ylim = board[0] // 2, board[1] // 2
    move = {'up': (0,1), 'down': (0,-1), 'left': (-1,0), 'right': (1,0)}
    
    for input in keyinput:
        dx, dy = move[input]
        
        if abs(x + dx) > xlim or abs(y + dy) > ylim:
            continue
        else:
            x, y = x + dx, y + dy
            
    return [x, y]
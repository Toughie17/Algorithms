def solution(code):
#     mode = 0
#     ret = []
    
#     for i in range(len(code)):
#         if mode == 0:
#             if code[i] != '1' and i % 2 == 0:
#                 ret.append(code[i])
#             elif code[i] == '1':
#                 mode = 1
        
#         elif mode == 1:
#             if code[i] != '1' and i % 2 == 1:
#                 ret.append(code[i])
#             elif code[i] == '1':
#                 mode = 0
    
#     return (''.join(ret) if ret else "EMPTY")

    # ;;;;
    return ''.join(code.split('1'))[::2] or "EMPTY"
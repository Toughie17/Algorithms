def solution(s):
#     if len(s) != 4 and len(s) != 6:
#         return False
    
#     for cha in s:
#         if not cha.isdigit():
#             return False
        
#     return True

    return s.isdigit() and len(s) in [4, 6]
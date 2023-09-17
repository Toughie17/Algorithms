def solution(before, after):
#     sol = list(before)
    
#     for cha in after:
#         if cha in sol:
#             sol.remove(cha)
            
#     return 1 if not sol else 0

    return 1 if sorted(before) == sorted(after) else 0
    # zzz
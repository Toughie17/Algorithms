def solution(s):
#     counts = {}
    
#     for cha in s:
#         if cha in counts:
#             counts[cha] += 1
#         else:
#             counts[cha] = 1
    
#     uniques = [cha for cha, count in counts.items() if count == 1]
    
#     return ''.join(sorted(uniques))

    #카운트를 왤케 까먹지
    return ''.join(sorted([cha for cha in s if s.count(cha) == 1]))
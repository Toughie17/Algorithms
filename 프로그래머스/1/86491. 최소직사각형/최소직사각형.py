def solution(sizes):
#     w = []
#     h = []
    
#     for size in sizes:
#         if size[0] >= size[1]:
#             w.append(size[0])
#             h.append(size[1])
#         else:
#             w.append(size[1])
#             h.append(size[0])
            
#     return max(w) * max(h)

    # sizes의 요소는 [숫자, 숫자] 이다.
    # 즉 요소를 하나씩 보면서 가장 큰 숫자를 모아(명함의 가로), 거기서 최대 값을 구하고 (케이스의 가로)
    # 요소 속에서 가장 작은 숫자를 모아(명함의 세로) 거기서 최대 값을 구한다.(케이스의 세로)
    return max(max(size) for size in sizes) * max(min(size) for size in sizes)
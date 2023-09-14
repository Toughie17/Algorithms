def solution(price):
    
#     if price >= 500000:
#         return int(price * 0.8)
#     elif price >= 300000:
#         return int(price * 0.9)
#     elif price >= 100000:
#         return int(price * 0.95)
#     else:
#         return price
    
    #
    table = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    
    for p, rate in table.items():
        if price >= p:
            return int(price * rate)
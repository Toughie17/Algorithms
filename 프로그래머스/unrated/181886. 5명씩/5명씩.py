def solution(names):
    # 나눈 배열을 담을 배열(2차원)   
#     divided_arr = []
    
#     # 5개씩 나눠서 divided_arr에 추가
#     for i in range(0, len(names), 5):
#         part = names[i: i+5]
#         divided_arr.append(part)
    
#     # divided_arr의 각 요소의 첫번째 요소 뽑기
#     return [ part[0] for part in divided_arr ]
    
    
    # 엄청 간단한 풀이 
    # 결국 처음부터 5개 간격으로 요소를 확인하는 것..
    return names[::5]
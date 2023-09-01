def solution(num_list):
    # 처음 풀이
#     odd_sum = sum(num_list[::2])
#     even_sum = sum(num_list[1::2])
    
#     if odd_sum > even_sum:
#         return odd_sum
#     elif odd_sum < even_sum:
#         return even_sum
#     else:
#         return odd_sum
    
    # 다른 풀이
#     odd_sum = 0
#     even_sum = 0
    
#     for i in range(len(num_list)):
#         if i % 2 == 0:
#             odd_sum += num_list[i]
#         else:
#             even_sum += num_list[i]
#     return max(odd_sum, even_sum)

    # 최적 풀이
    # max(홀수의 합, 짝수의 합)
    return max(sum(num_list[::2]),sum(num_list[1::2]) )
    
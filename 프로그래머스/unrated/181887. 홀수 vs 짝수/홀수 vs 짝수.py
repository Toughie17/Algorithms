def solution(num_list):
    # 처음 풀이 슬라이싱 과정에서 배열을 2번 순회해야함.
#     odd_sum = sum(num_list[::2])
#     even_sum = sum(num_list[1::2])
    
#     if odd_sum > even_sum:
#         return odd_sum
#     elif odd_sum < even_sum:
#         return even_sum
#     else:
#         return odd_sum
    
    # 더 효율적인 풀이 
    # 인덱스를 통해 배열을 1번만 순회해도 됨.
    odd_sum = 0
    even_sum = 0
    
    for i in range(len(num_list)):
        if i % 2 == 0:
            odd_sum += num_list[i]
        else:
            even_sum += num_list[i]
    return max(odd_sum, even_sum)
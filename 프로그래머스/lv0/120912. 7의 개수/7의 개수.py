def solution(array):
#     count = 0
    
#     for num in array:
#         for ele in str(num):
#             if ele == '7':
#                 count += 1
#     return count

    # return str(array).count('7')

    return ''.join(map(str,array)).count('7')
def solution(arr1, arr2):
    
#     if len(arr1) > len(arr2):
#         return 1
    
#     elif len(arr1) < len(arr2):
#         return -1
    
#     elif len(arr1) == len(arr2):
#         leftSum = sum(arr1)
#         rightSum = sum(arr2)
#         if leftSum > rightSum:
#             return 1
#         elif leftSum < rightSum:
#             return -1
#         else:
#             return 0
    
    # 배열의 길이 비교 긴 쪽이 더 큼
    # 길이가 같다면 원소의 합 비교
    # 왼쪽이 크면 1, 같으면 0, 오른쪽이 크면 -1
    
    #부울 표현식을 정수로 변환하면 True는 1, False는 0이다. 
    
    return (len(arr1) > len(arr2)) - (len(arr2) > len(arr1)) or (sum(arr1) > sum(arr2)) - (sum(arr2) > sum(arr1))
    #문제 설명에서 1, 0, -1을 준 이유가 이거였나..
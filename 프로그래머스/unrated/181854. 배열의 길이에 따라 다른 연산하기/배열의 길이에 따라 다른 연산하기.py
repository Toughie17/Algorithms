def solution(arr, n):
    
#     result = []
    
#     if len(arr) % 2 == 1:
#         for index, value in enumerate(arr):
#             if index % 2 == 0:
#                 result.append(value + n)
#             else:
#                 result.append(value)
#         return result
    
#     else:
#         for index, value in enumerate(arr):
#             if index % 2 == 1:
#                 result.append(value + n)
#             else:
#                 result.append(value)
#         return result
    
    # 배열 길이
    N = len(arr)
    
    # 배열 홀수인 경우 (1은 true, 0은 false임)
    if N % 2:
        # 인덱스를 구하기. 짝수 인덱스가 필요하기 때문에 0부터,N까지, 2칸 간격으로( 0, 2, 4...)
        #길이가 5인 배열의 마지막 인덱스는 4번이다. 따라서 range의 형태는 range(0,N)이 되는 것
        for i in range(0,N,2):
            arr[i] += n
        return arr
    # 배열 짝수인 경우
    else:
        # 인덱스 구하기. 홀수 인덱스가 필요하다.
        #그래서 1부터 2칸 간격으로 
        for i in range(1,N,2):
            arr[i] += n
        return arr
            

'''
arr은 함수 solution의 매개변수로 전달되는 변수이기 때문에 함수 내부에서 계속해서 사용할 수 있습니다. 함수 내부에서 arr은 해당 함수의 스코프 내에서 유효한 지역 변수로 취급됩니다. 함수가 호출될 때 파라미터로 전달된 값을 저장하고, 함수 내에서 필요한 곳에서 이 값을 사용할 수 있습니다. 함수가 종료되면 이 지역 변수는 사라집니다.
'''
def solution(numbers, k):
#     num = 1
#     index = 0
#     count = 0
    
#     while count < k:
#         next  = index + 2
        
#         #2인데 4로 가야됨 근데 4는 범위를 벗어남. (한 칸 모자란 상황)
#         if next == len(numbers):
#             index = 0
#             num = numbers[index]
#         #2인데 4로 가야됨 2칸 모자라는 상황
#         elif next == len(numbers) - 1:
#             index = 1
#             num = numbers[index]
        
#         index = next
#         num = numbers[index]
#         count += 1
    
#     return num

#나머지 개념 활용해보자.
    idx = 0
    #3번째로 던질 사람인 경우 2번 던지고 나서 현 위치의 사람을 말함.
    #반복문으로 2번만 던지면 됨(k-1)
    for i in range(k-1):
        idx = (idx + 2) % len(numbers)
        #0, 2, 4, 0, 2, 4
        #0, 2, 1,  0, 2, 1
    return numbers[idx]

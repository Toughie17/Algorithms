#약수를 구하는 함수를 만들 수도 있지만 숫자가 커지면 비효율적이다.
# def count(n):
#     count = 0
#     for i in range(1, n+ 1):
#         if n % i == 0:
#             count += 1
#     return count
import math

def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        if math.sqrt(num).is_integer():
            answer -= num
        else:
            answer += num
    return answer
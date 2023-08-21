from functools import reduce

def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        return multiply(num_list)
    
        # 곱하기 직접 구현
        # result = 1
        # for num in num_list:
        #     result *= num
        # return result
    
def multiply(arr):
    return reduce(lambda x, y: x * y, arr)

# reduce는 리스트의 두 아이템(원소)에 함수를 왼쪽에서 오른쪽으로 누적적으로 적용해서 하나의 단일 값으로 줄인다.
# 이상, 이하, 미만, 초과 조건을 잘 확인하자.
'''
all은 파이썬 내장 함수 중 하나로, 주어진 반복 가능한(iterable) 객체(리스트, 튜플, 문자열 등)의 모든 요소가 참(True)인지 확인하는 역할을 합니다. 만약 해당 반복 가능한 객체의 모든 요소가 참이면 all 함수는 True를 반환하고, 그렇지 않으면 False를 반환합니다.
'''

# def solution(l,r):
#     result = []
    
#     for num in range(l, r+1):
#         if all(digit in '05' for digit in str(num)):
#             result.append(num)
            
#     return (sorted(result) if result else [-1])

# set 활용법

def solution(l,r):
    result = []
    for num in range(l, r + 1):
        #같은 배열끼리 - 연산하면 {}이 되니, False가 되고 즉 0,5로만 이루어져 있다는 뜻
        if not set(str(num)) - set(['0', '5']):
            result.append(num)
            
    return sorted(result) if result else [-1]
            
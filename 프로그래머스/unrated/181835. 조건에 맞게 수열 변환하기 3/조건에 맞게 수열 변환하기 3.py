def solution(arr, k):
    if k % 2 == 1:
        return [num * k for num in arr]
    else:
        return [num + k for num in arr]
        
# new_list = [expression for item in iterable if condition]
# even_numbers = [x for x in range(1, 11) if x % 2 == 0]
# iterable: 반복 가능한(iterable) 객체, 예를 들어 리스트, 튜플, 범위(range), 문자열 등이 될 수 있습니다.

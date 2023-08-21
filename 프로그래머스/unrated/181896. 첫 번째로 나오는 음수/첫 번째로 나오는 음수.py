def solution(num_list):
    for index, num in enumerate(num_list):
        if num < 0:
            return index
    return -1

#enumerate는 index, 요소의 튜플을 반환합니다.

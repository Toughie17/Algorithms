def solution(my_string, is_prefix):
    # return int(is_prefix in my_string)
    # return int(my_string.startswith(is_prefix))

# 특정 접두사로 시작하는 지 검사하는 데 사용되는 문자열 메서드 startswith

# 만약 메서드를 몰랐다면

    if my_string[:len(is_prefix)] == is_prefix:
        return 1
    return 0
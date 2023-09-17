def solution(my_string):
    # return ''.join(sorted([alpha.lower() for alpha in my_string]))
    # 이미 스트링 타입은 iterable이니까 ㅎ..
    return ''.join(sorted(my_string.lower()))
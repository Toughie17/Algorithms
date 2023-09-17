def solution(my_string):
    return ''.join(sorted([alpha.lower() for alpha in my_string]))
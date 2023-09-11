def solution(my_string, overwrite, s):
    result = list(my_string)
    result[s:len(overwrite) + s] = overwrite
    return ''.join(result)
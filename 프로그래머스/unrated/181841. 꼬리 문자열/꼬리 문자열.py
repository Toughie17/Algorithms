def solution(str_list, ex):
    result = ""
    for str in str_list:
        if ex not in str:
            result += str
    return result
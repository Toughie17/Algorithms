def solution(my_string, alp):
    #replace
    if alp in my_string:
        return my_string.replace(alp, alp.upper())
    return my_string
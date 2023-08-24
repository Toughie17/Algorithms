def solution(my_string, alp):
    # replace
    
    # if alp in my_string:
    #     return my_string.replace(alp, alp.upper())
    # return my_string
    # 바꿀문자열.replace(이전, 바꿀것, 개수(디폴트는 전부))
    # 만약 바꿀 것이 바꿀 문자열에 없다면 바꿀문자열을 그대로 return
    return my_string.replace(alp, alp.upper())
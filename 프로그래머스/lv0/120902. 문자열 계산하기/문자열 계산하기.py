def solution(my_string):
    # return eval(my_string)
    return sum(map(int,my_string.replace(' - ', ' + -').split('+')))
    # "3 + 4 - 7 - 8"
    # "3 + 4 + -7 + -8"


    
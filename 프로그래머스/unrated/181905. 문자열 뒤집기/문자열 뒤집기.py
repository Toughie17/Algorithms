def solution(my_string, s, e):
    part = my_string[s: e+1][::-1]
    return my_string[:s] + part + my_string[e+1:]
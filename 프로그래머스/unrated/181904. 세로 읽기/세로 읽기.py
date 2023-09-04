def solution(my_string,m,c):
    result = []
    #결국은 c번째 문자부터 m간격으로 떨어진 애들의 조합임.
    for i in range(c-1, len(my_string), m):
        result.append(my_string[i])
    return ''.join(result)
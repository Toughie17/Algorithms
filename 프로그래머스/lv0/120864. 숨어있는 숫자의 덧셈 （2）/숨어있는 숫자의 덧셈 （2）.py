def solution(my_string):
    
    #문자열은 immutable, replace하면 새로운 문자열이 생성됨
    for i in my_string:
        if i.isalpha():
            my_string = my_string.replace(i, ' ')
            
    return sum(map(int, my_string.split()))
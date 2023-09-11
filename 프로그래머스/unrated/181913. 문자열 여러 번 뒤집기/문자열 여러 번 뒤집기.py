def solution(my_string, queries):
    result = list(my_string)
    
    for (s, e) in (queries):
        result[s : e + 1] = result[s : e + 1][::-1]
        
    return ''.join(result)
        
#파이썬에서 문자열은(immutable) 즉 불변 타입으로 직접 인덱스를 통해 문자열 내용 변경 불가
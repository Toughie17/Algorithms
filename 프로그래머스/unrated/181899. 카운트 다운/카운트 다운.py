def solution(start, end_num):
    
    return sorted([x for x in range(end_num, start+1)], reverse = True)
    
#     list = [ x for x in range(end_num, start +1) ]
#     answer = sorted(list, reverse = True)
#     return answer

# sort()는 리스트를 제자리에서 수정(원래 변수 수정) -> 반환값이 None이다! 
# sorted()는 반환값이 배열값! 원래 변수는 수정되지 않는다.

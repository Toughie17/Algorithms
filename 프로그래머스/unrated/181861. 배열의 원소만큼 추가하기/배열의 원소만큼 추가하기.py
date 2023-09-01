# from collections import Counter

def solution(arr):
    #2중 반복문 사용 O(N2)
    # result = []
    # for i in (arr):
    #     for j in range(i):
    #         result.append(i)
    # return result
    
    #반복문 한번만
    result = []
    for num in arr:
        result.extend([num] * num)
    return result

    '''
    list.append(x)는 리스트 끝에 x를 그대로 넣는다.
    x = ['a', 'b', 'c']
    y = ['애','플']
    x.append(y)의 결과는
    ['a', 'b', 'c', ['애','플']]
    
    list.extend(iterable)은 리스트 끝에 가장 바깥쪽 iterable의 모든 항목을 넣는다.
    (iterable이 2중 배열일 경우, 내부 배열만 추가됨, 1중 배열인 경우 내부 요소들만 추가됨)
    x.extend(y)의 결과는
    ['a', 'b','c','애','플']
    
    '''
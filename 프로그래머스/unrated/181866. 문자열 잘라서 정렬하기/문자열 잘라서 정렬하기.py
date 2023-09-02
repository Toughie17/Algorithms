def solution(myString):
    return sorted([str for str in myString.split('x') if str])
    #빈문자열은 False!
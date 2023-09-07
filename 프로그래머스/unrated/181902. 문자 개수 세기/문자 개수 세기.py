# ord() 함수는 문자(character)를 해당하는 유니코드 코드 포인트(정수)로 변환하는 파이썬 내장 함수

def solution(my_string):
#     counts = [0] * 52
    
#     for cha in my_string:
#         #0번부터 25번까지 대문자 26개
#         if 'A' <= cha <= 'Z':
#             counts[ord(cha) - ord('A')] += 1
#         #26번부터 51번까지 소문자 26개
#         elif 'a' <= cha <= 'z':
#             counts[ord(cha) - ord('a') + 26] += 1
    
#     return counts


    result = [0] * 52
    for cha in my_string:
        if cha.isupper():
            result[ord(cha) - 65] += 1
        else:
            result[ord(cha) - 71] += 1
    return result

'''
ord('A') = 65
ord('a') = 97
'''
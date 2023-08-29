def solution(myString):
#     answer = ''
    
#     for cha in myString:
#         if cha == 'a':
#             answer += "A"
#         elif cha != "A" and cha.isupper():
#                 answer += cha.lower()
#         else: answer += cha
                
#     return answer

    # 결국 대문자는 A만 남기고 나머지는 다 소문자로 바꾸겠다는 말이니
    return myString.lower().replace('a', 'A')
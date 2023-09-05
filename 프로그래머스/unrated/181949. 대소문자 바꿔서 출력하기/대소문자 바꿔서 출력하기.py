str = input().strip()
# print(str.swapcase())

# for cha in str:
#     if cha.isupper():
#         print(cha.lower(), end = '')
#     else:
#         print(cha.upper(), end = '')

answer = []
for cha in str:
    if cha.isupper():
        answer.append(cha.lower())
    else:
        answer.append(cha.upper())
        
print(''.join(answer))

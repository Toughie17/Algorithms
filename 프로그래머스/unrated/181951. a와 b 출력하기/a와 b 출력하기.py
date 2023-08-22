# a, b = map(int, input().strip().split(' '))
# print(a + b)

# 입력 받고, 양쪽 공백 제거 후, 공백을 기준으로 split -> 각각의 정수가 담긴 리스트
# map을 통해 리스트의 각 요소를 int로 형변환 한 뒤에 a, b에 할당
# 문자열 포메팅 방식. %, {}.format(), f {}

a, b = map(int, input().strip().split())
# print('a = %s\nb = %s'%(a,b))
# print('a = {}\nb = {}'.format(a,b))
print(f'a = {a}\nb = {b}')
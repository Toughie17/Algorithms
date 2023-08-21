def solution(number, n, m):
    if number % n == 0 and number % m == 0:
        return 1
    else:
        return 0
# 논리연산자 AND 두 조건이 모두 참일 때만 전체 표현식이 참이 됨.
# & 비트 AND연산자. 비트 단위로 AND 연산을 수행하며, 이진수로 나타낸 각 비트가 모두 1일 때만 결과가 1

#조건을 검사할 때는 논리 연산자인 and를 사용하자!

def solution(ineq, eq, n, m):
#     if (ineq == '>' and eq == '=' and n >= m):
#         return 1
#     elif (ineq == '<' and eq == '=' and n <= m):
#         return 1
#     elif (ineq == '>' and eq == '!' and n > m):
#         return 1
#     elif (ineq == '<' and eq == '!' and n < m):
#         return 1
    
#     return 0

    # 평가식을 이용하는 방법
    # eval은 파이썬에서 문자열로 표현된 파이썬 코드를 실행하는 내장 함수
    return int(eval((str(n)+ineq+eq).replace('!', '')+ str(m)))
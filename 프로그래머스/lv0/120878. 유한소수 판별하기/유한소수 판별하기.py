#유클리드 호제법을 활용한 최대 공약수 구하기
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solution(a, b):
    #최대 공약수
    b /= gcd(a,b)
    #기약분수
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5
        
    return 1 if b == 1 else 2
    

import math
def solution(numer1, denom1, numer2, denom2):
    #분모의 최소 공배수를 구해야함.
    gcd = math.gcd(denom1, denom2)
    lcd = (denom1 * denom2) // gcd
    
    upper = (numer1 * lcd // denom1) + (numer2 * lcd // denom2)
    
    gcd2 = math.gcd(upper, lcd)
    
    return [upper // gcd2, lcd // gcd2]
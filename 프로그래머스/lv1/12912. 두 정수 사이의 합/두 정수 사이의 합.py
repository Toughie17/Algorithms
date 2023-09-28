def solution(a, b):
    if a <= b:
        return sum([x for x in range(a,b + 1)])
    elif a > b:
        return sum([x for x in range(b,a + 1)])
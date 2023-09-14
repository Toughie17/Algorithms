def solution(sides):
    long = max(sides)
    sides.remove(long)
    return 1 if long < sum(sides) else 2
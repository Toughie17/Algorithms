def solution(sides):
    # long = max(sides)
    # sides.remove(long)
    # return 1 if long < sum(sides) else 2

    return 1 if max(sides) < (sum(sides) - max(sides)) else 2
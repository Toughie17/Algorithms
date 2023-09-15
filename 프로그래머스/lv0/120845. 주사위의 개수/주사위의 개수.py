def solution(box, n):
    # result = 1
    # for l in box:
    #     result *= l // n
    # return result

    x, y, z = box
    return (x // n) * (y // n) * (z // n)
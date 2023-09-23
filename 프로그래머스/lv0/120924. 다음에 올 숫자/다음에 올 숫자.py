def solution(data):
#     if data[1] - data[0] == data[2] - data[1]:
#         return data[-1] + data[1] - data[0]
#     else:
#         return data[-1] * (data[1] / data[0])

    #common의 길이가 2 초과니까 최소 원소는 3개 이상이다.
    a, b, c = data[:3]
    if (b-a) == (c-b):
        return data[-1] + (b-a)
    elif (b/a) == (c/b):
        return data[-1] * (b/a)
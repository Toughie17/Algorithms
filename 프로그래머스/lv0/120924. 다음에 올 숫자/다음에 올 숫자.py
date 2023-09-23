def solution(data):
    
    if data[1] - data[0] == data[2] - data[1]:
        return data[-1] + data[1] - data[0]
    else:
        return data[-1] * (data[1] / data[0])
def solution(s):
    test = []
    answer = []

    for cha in s:
        if cha in test:
            test.append(cha)
            idx = ([index for index, value in enumerate(test) if value == cha])
            answer.append(idx[-1] - idx[-2])
        else:
            test.append(cha)
            answer.append(-1)
            
    return answer
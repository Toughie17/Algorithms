def solution(strArr):
    # for i in range(0, len(strArr), 2):
    #     strArr[i] = strArr[i].lower()
    # for  in range(1, len(strArr), 2):
    #     strArr[i] = strArr[i].upper()
    # return strArr

#런타임 에러 발생

    result = []
    for i in range(len(strArr)):
        if i % 2 == 1:
            result.append(strArr[i].upper())
        else:
            result.append(strArr[i].lower())
    return result

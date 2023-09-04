def solution(intStrs, k, s, l):
    result = []
    
    for str in intStrs:
        num = int(str[s:s +l])
        if num > k:
            result.append(num)
    return result
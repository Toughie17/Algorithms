def solution(myString, pat):
    count = 0
    for i in range(len(myString)):
        if pat in myString[i:len(pat) + i]:
            count += 1
    return count
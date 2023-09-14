def solution(s1, s2):
    # sol = 0
    # for num in s1:
    #     if num in s2:
    #         sol += 1
    # return sol

#교집합으로 생각하면..

    return len(set(s1) & set(s2))
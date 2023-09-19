def solution(spell, dic):
    #한 번씩만 써야한다? 알파벳 순으로 정렬했을 때 더 길거나 중복되는 것이 있으면 같지 않을 것
    for d in dic:
        if sorted(d) == sorted(spell):
            return 1
    return 2
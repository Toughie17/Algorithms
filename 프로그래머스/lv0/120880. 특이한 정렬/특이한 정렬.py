def solution(numlist,n):
    # distance = [(abs(n - x), x) for x in numlist]
    # distance.sort(key= lambda x: (x[0], -x[1]))
    # return [x[1] for x in distance]
    
    return sorted(numlist, key = lambda x: (abs(n - x), n - x))
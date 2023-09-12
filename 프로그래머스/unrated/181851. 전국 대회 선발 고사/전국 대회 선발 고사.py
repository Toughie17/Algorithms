def solution(rank, attendance):
    
    arr = sorted([(r, num) for (num, r) in enumerate(rank) if attendance[num]])
    #[ (몇등, 몇번)]
    return 10000 * arr[0][1] + 100 * arr[1][1] + arr[2][1]
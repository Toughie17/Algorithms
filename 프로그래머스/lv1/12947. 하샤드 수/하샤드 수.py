def solution(x):
    total = sum(map(int,list(str(x))))
    
    # return x % sum(int(n) for n in str(x)) == 0
    return x % total == 0

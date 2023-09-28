def solution(x):
    total = sum(map(int,list(str(x))))
    
    if x % total == 0:
        return True
    return False
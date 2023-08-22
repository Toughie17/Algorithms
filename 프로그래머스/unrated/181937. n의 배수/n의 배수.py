def solution(num, n):
    if num % n == 0:
        return 1
    return 0
    
    # 짝수일 경우 num & n이 0이 되고, not을 통해 true가 되고 int(true)는 1
    # 홀수일 경우 num % n이 정수가 되고, not을 통해 false가 되고 int(false)는 0
    # return int(not(num % n))
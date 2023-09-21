def solution(A,B):
    count = 0
    
    #같아 질 때까지 밀거야
    while A != B:
        #A 길이만큼 다 밀어봤는데(한 바퀴 돌았는데) 안 같으면 안 되는거임
        if count > len(A):
            return -1
        #한 칸 씩 밀자
        A = A[-1] + A[:-1]
        count += 1
        
    return count
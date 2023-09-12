def solution(rank, attendance):
    answer = 0
    count = 0
    
    for i in range(1, len(rank) + 1):
        student_num = rank.index(i) #해당 값의 인덱스가 어디인가
        if attendance[student_num]:
            answer += student_num * 100 ** (2 - count)
            count += 1
        if count == 3:
            break
    
    return answer
        
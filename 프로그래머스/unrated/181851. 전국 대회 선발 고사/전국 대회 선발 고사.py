def solution(rank, attendance):
    # answer = 0
    answer = []
    count = 0
    
    for i in range(1, len(rank) + 1):
        student_num = rank.index(i) #해당 값의 인덱스가 어디인가
        if attendance[student_num]:
            # answer += student_num * 100 ** (2 - count)
            answer.append(student_num)
            count += 1
        if count == 3:
            break
    
    return (10000 * answer[0] + 100 * answer[1] + answer[2])


'''
결국 rank에는 1등부터 n등까지 있다.
1등,2등,3등.. 이런 식으로 등수가 높은 학생 3명만 필요함.
다만 정렬이 안되어 있기 때문에, 우선 1등 학생을 찾는다.
그리고 1등 학생의 번호(index)를 알아낸다.(.index를 활용해서)
해당 학생이 참석 가능한지 attendance의 인덱싱을 통해(학생 번호로) 확인 후
참석 가능하면 정답 배열에 추가한다. (바로 수식을 사용해도 되고)
총 3명을 찾으면 종료한다.
'''
        
def solution(rank, attendance):
    
    arr = sorted([(r, num) for (num, r) in enumerate(rank) if attendance[num]])
    #[ (몇등, 몇번)]
    return 10000 * arr[0][1] + 100 * arr[1][1] + arr[2][1]

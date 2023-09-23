def solution(lines):
    #끝점과 시작점이 같으면 선분이 겹치는 것이 아님. 교집합으로 처리하면 안 됨.
    #그래서 그냥 꼬리를 잘라서 처리
    sets = [set(range(min(l), max(l))) for l in lines]
    #각 선분의 교집합의 길이를 구한다(숫자 카운팅) 그리고 합집합을 통해 중복을 제거한다.
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])
def solution(food):
# 물을 기준으로 좌우 대칭, 칼로리 낮은 순으로 되어 있음
# 각 음식의 개수는 무조건 짝수여야함.
    left = ''
    for i in range(1, len(food)):
        left += str(i) * (food[i] // 2)
    
    #문자열 역순으로 바꿔서 더해주기
    return left + '0' + left[::-1]
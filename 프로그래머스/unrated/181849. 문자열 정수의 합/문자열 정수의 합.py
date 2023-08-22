def solution(num_str):
    result = 0
    for num in num_str:
        result += int(num)
    return result

'''
# 숫자로 된 문자열을 정수로 변환하는 함수
def str_to_int(s):
    return int(s)

# 숫자로 된 문자열 리스트
num_str_list = ["1", "2", "3", "4", "5"]

# map()을 사용하여 각 문자열을 정수로 변환
int_list = list(map(str_to_int, num_str_list))

# 결과 출력
print(int_list)

'''

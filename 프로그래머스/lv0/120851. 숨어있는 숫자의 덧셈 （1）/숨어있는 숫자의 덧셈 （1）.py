def solution(my_string):
    sol = []
    # sol = 0
    for ele in my_string:
        # 정수형인지 .isdigit()
        if ele.isdigit():
        # if isinstance(int(ele), int):  value error 발생 가능성
            sol.append(int(ele))
            # sol += int(ele)
    return sum(sol)
        
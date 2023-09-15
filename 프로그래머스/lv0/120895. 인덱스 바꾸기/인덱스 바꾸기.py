def solution(my_string, num1, num2):
    sol = list(my_string)
    sol[num1], sol[num2] = sol[num2], sol[num1]
    return ''.join(sol)
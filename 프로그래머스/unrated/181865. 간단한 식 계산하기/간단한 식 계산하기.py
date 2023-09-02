def solution(binomial):
    a, op, b = binomial.split()
    num1, num2 = int(a), int(b)
    
    # if op == '+':
    #     return num1 + num2
    # elif op == '-':
    #     return num1 - num2
    # else:
    #     return num1 * num2

    operators = {'+': num1 + num2, '-': num1 - num2, '*': num1 * num2}
    if op in operators:
        return operators[op]
    
    #내장함수 사용
    # return eval(binomial)
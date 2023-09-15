def solution(numbers):
    #0, 음수, 양수
    result = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            result.append(numbers[i] * numbers[j])
            
    return max(result)
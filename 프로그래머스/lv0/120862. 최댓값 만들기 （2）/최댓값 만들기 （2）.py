def solution(numbers):
    #0, 음수, 양수
    # result = []
    # for i in range(len(numbers)):
    #     for j in range(i + 1, len(numbers)):
    #         result.append(numbers[i] * numbers[j])
            
    # 
    sort = sorted(numbers)
    return max(sort[0] * sort[1], sort[-1] * sort[-2])
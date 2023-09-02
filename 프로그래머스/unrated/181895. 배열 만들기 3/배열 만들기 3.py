def solution(arr, intervals):
    result = []
    for i in range(len(intervals)):
        result.extend(arr[intervals[i][0]: intervals[i][1] + 1])
    return result
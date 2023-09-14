def solution(numbers):
    #내림차순으로 정렬 후 앞 두개를 곱하면 되지만, 0인 경우가 있을 수 있음.
    arr = sorted(numbers, reverse = True)
    return arr[0] * arr[1]
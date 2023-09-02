def solution(number):
    #return int(number) % 9
    nums = [int(num) for num in number]
    return sum(nums) % 9
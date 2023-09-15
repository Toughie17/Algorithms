def solution(numbers, direction):
    
    #오른쪽이면 맨 뒤에가 앞으로
    if direction == 'right':
        return [numbers[-1]] + numbers[:-1]
    #왼쪽이면 맨 앞이 맨 뒤로
    elif direction == 'left':
        return numbers[1:] + [numbers[0]]
    
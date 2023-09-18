def solution(numbers):
    #이걸 어떻게 쪼개지
    #쪼개는게 아니라 키값이 될 때까지 순회하는 거구나
    wordToNum = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    
    result = ''
    current = ''
    
    for cha in numbers:
        current += cha
        if current in wordToNum:
            result += wordToNum[current]
            current = ''
            
    return int(result)
    
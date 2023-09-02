def solution(my_strings, parts):
    
    result = ''
    
    for index, string in enumerate(my_strings):
        result += string[parts[index][0]: parts[index][1] + 1]
        
    return result
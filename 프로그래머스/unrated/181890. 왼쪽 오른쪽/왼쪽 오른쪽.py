def solution(str_list):
    
    for index, cha in enumerate(str_list):
        if cha == "l":
            return str_list[:index]
        elif cha == 'r':
            return str_list[index+ 1:]
            
    return []
    
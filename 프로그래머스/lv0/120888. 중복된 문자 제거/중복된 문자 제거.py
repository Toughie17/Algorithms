def solution(my_string):
    answer = []
    
    for cha in my_string:
        if cha in answer:
            continue
        else:
            answer.append(cha)
            
    return ''.join(answer)
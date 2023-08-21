def solution(rny_string):
    
    answer = ''
    for cha in rny_string:
        if cha == 'm':
            answer += 'rn'
        else:
            answer += cha
    return answer

    # answer = []
    # for cha in rny_string:
    #     if cha == 'm':
    #         answer.append('rn')
    #     else:
    #         answer.append(cha)
    # answer = ''.join(answer)
    # return answer
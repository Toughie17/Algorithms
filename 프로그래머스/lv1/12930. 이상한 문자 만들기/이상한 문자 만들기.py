def solution(s):
    splitted = s.split(" ")
    answer = []
#처음에는 매개변수 없이 s.split -> 
#그 이유는 s에 공백을 포함한 문자가 들어오면 마지막에 그 공백도 출력해줘야 한다.
    for word in splitted:
        temp = ''
        for i in range(len(word)):
            if i % 2 == 0:
                temp += word[i].upper()
            else:
                temp += word[i].lower()
        answer.append(temp)
        
    return ' '.join(answer)
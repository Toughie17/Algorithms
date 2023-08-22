def solution(n, control):
    
    answer = n
    
    for con in control:
        if con == "w":
            answer += 1
        elif con == 's':
            answer -= 1
        elif con == 'd':
            answer += 10
        else:
            answer -= 10
            
    return answer

'''
딕셔너리 활용
dic = {'w': 1, 's': -1, 'd': 10, 'a': -10}
for con in control:
    answer += dic[con]
'''

'''
참신한 풀이법
return n + 10 * (control.count('d') - control.count('a')) + (control.count('w') - control.count('s'))
'''

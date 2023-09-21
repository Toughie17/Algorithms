def solution(id_pw, db):
    
    for info in db:
        if id_pw[0] in info:
            if id_pw[1] == info[1]:
                return "login"
            return 'wrong pw'
    return 'fail'

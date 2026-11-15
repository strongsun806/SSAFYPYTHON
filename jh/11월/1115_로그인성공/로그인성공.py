def solution(id_pw, db):
    answer = 'login'
    id = []
    pw = []
    for i in range(len(db)):
        id.append(db[i][0])
        pw.append(db[i][1])
    if id_pw[0] not in id:
        answer = 'fail'
    elif pw[id.index(id_pw[0])] != id_pw[1]:
        answer = 'wrong pw'
    return answer
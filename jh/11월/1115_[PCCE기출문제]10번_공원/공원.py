def solution(mats, park):
    answer  = -1
    r = len(park)
    c = len(park[0])

    for size in sorted(mats, reverse=True):
        for i in range(r - size + 1):
            for j in range(c - size + 1):
                ok = True
                for di in range(size):
                    for dj in range(size):
                        if park[i + di][j + dj] != '-1':
                            ok = False
                            break
                    if not ok:
                        break
                if ok:
                    return size
    return answer


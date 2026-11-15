import sys
sys.stdin = open('sample_input.txt', 'r')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(idx, cnt, length):
    global best_cnt, best_len

    if cnt + (m - idx) < best_cnt:
        return

    if idx == m:
        if cnt > best_cnt or (cnt == best_cnt and length < best_len):
            best_cnt = cnt
            best_len = length
        return

    r, c = cores[idx]

    for d in range(4):
        path = []
        nr = r + dr[d]
        nc = c + dc[d]
        ok = True
        while 0<=nr<n and 0<=nc<n:
            if arr[nr][nc] != 0:
                ok = False
                break
            path.append((nr, nc))
            nr += dr[d]
            nc += dc[d]

        if ok:
            for pr, pc in path:
                arr[pr][pc] = 2
            dfs(idx+1, cnt+1, length+len(path))
            for pr, pc in path:
                arr[pr][pc] = 0

    dfs(idx+1,cnt, length)


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    cores = []
    for i in range(1, n-1):
        for j in range(1, n-1):
            if arr[i][j] == 1:
                cores.append((i, j))
    m = len(cores)
    best_cnt = 0
    best_len = 0
    dfs(0, 0, 0)

    print(f'#{tc} {best_len}')
from collections import deque
import sys
sys.stdin = open('sample_input.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
opp = [1, 0, 3, 2]

pipe = {
    1:[0, 1, 2, 3],
    2:[0, 1],
    3:[2, 3],
    4:[0, 3],
    5:[1, 3],
    6:[1, 2],
    7:[0, 2],
}

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    time = [[0]*M for _ in range(N)]
    time[R][C] = 1
    q = deque([(R, C)])
    cnt = 1

    while q:
        r, c = q.popleft()
        if time[r][c] == L:
            continue
        for d in pipe[grid[r][c]]:
            nr, nc = r + dr[d], c + dc[d]
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if grid[nr][nc] == 0 or time[nr][nc]:
                continue
            if opp[d] not in pipe[grid[nr][nc]]:
                continue
            time[nr][nc] = time[r][c] + 1
            cnt += 1
            q.append((nr, nc))
    print(f'#{tc} {cnt}')
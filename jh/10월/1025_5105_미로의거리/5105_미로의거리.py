import sys
sys.stdin = open('sample_input.txt')

from collections import deque

def bfs(r, c, cnt):
    global ans
    q = deque()
    q.append((r,c,cnt))
    visited[r][c] = 1
    while q:
        sr, sc, cnt = q.popleft()
        if arr[sr][sc] == 3:
            ans = cnt - 1
            return
        for d in range(4):
            nr = sr + dr[d]
            nc = sc + dc[d]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and arr[nr][nc] != 1:
                q.append((nr, nc, cnt + 1))
                visited[nr][nc] = 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    ans = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                bfs(i, j, 0)
    print(f'#{tc} {ans}')
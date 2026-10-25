import sys
sys.stdin = open('sample_input.txt', 'r')

from collections import deque

def bfs(r, c):
    queue = deque()
    queue.append((r, c))
    visited[r][c] = 1
    while queue:
        sr, sc = queue.popleft()

        if visited[sr][sc] >= t:
            break

        if arr[sr][sc] == 1:
            dr = [-1,1,0,0]
            dc = [0,0,-1,1]
            for d in range(4):
                nr = sr + dr[d]
                nc = sc + dc[d]
                if 0 <= nr < N and 0 <= nc < M \
                      and visited[nr][nc] == 0 and arr[nr][nc] != 0:
                    if dr[d] == -1 and arr[nr][nc] not in (1, 2, 5, 6):
                        continue
                    if dr[d] == 1 and arr[nr][nc] not in (1, 2, 4, 7):
                        continue
                    if dc[d] == -1 and arr[nr][nc] not in (1, 3, 4, 5):
                        continue
                    if dc[d] == 1 and arr[nr][nc] not in (1, 3, 6, 7):
                        continue
                    queue.append((nr, nc))
                    visited[nr][nc] = visited[sr][sc] + 1
    
        if arr[sr][sc] == 2:
            dr = [-1,1]
            dc = [0,0]
            for d in range(2):
                nr = sr + dr[d]
                nc = sc + dc[d]
                if 0 <= nr < N and 0 <= nc < M \
                      and visited[nr][nc] == 0 and arr[nr][nc] != 0:
                    if dr[d] == -1 and arr[nr][nc] not in (1, 2, 5, 6):
                        continue
                    if dr[d] == 1 and arr[nr][nc] not in (1, 2, 4, 7):
                        continue
                    
                    queue.append((nr, nc))
                    visited[nr][nc] = visited[sr][sc] + 1
    
        if arr[sr][sc] == 3:
            dr = [0,0]
            dc = [-1,1]
            for d in range(2):
                nr = sr + dr[d]
                nc = sc + dc[d]
                if 0 <= nr < N and 0 <= nc < M \
                      and visited[nr][nc] == 0 and arr[nr][nc] != 0:
                    if dc[d] == -1 and arr[nr][nc] not in (1, 3, 4, 5):
                        continue
                    if dc[d] == 1 and arr[nr][nc] not in (1, 3, 6, 7):
                        continue

                    queue.append((nr, nc))
                    visited[nr][nc] = visited[sr][sc] + 1
    
        if arr[sr][sc] == 4:
            dr = [-1,0]
            dc = [0,1]
            for d in range(2):
                nr = sr + dr[d]
                nc = sc + dc[d]
                if 0 <= nr < N and 0 <= nc < M \
                      and visited[nr][nc] == 0 and arr[nr][nc] != 0:
                    if dr[d] == -1 and arr[nr][nc] not in (1, 2, 5, 6):
                        continue
                    if dc[d] == 1 and arr[nr][nc] not in (1, 3, 6, 7):
                        continue

                    queue.append((nr, nc))
                    visited[nr][nc] = visited[sr][sc] + 1
    
        if arr[sr][sc] == 5:
            dr = [1,0]
            dc = [0,1]
            for d in range(2):
                nr = sr + dr[d]
                nc = sc + dc[d]
                if 0 <= nr < N and 0 <= nc < M \
                      and visited[nr][nc] == 0 and arr[nr][nc] != 0:
                    if dr[d] == 1 and arr[nr][nc] not in (1, 2, 4, 7):
                        continue
                    if dc[d] == 1 and arr[nr][nc] not in (1, 3, 6, 7):
                        continue
                    queue.append((nr, nc))
                    visited[nr][nc] = visited[sr][sc] + 1
    
        if arr[sr][sc] == 6:
            dr = [1,0]
            dc = [0,-1]
            for d in range(2):
                nr = sr + dr[d]
                nc = sc + dc[d]
                if 0 <= nr < N and 0 <= nc < M \
                      and visited[nr][nc] == 0 and arr[nr][nc] != 0:
                    if dr[d] == 1 and arr[nr][nc] not in (1, 2, 4, 7):
                        continue
                    if dc[d] == -1 and arr[nr][nc] not in (1, 3, 4, 5):
                        continue
                    queue.append((nr, nc))
                    visited[nr][nc] = visited[sr][sc] + 1
    
        if arr[sr][sc] == 7:
            dr = [-1,0]
            dc = [0,-1]
            for d in range(2):
                nr = sr + dr[d]
                nc = sc + dc[d]
                if 0 <= nr < N and 0 <= nc < M \
                      and visited[nr][nc] == 0 and arr[nr][nc] != 0:
                    if dr[d] == -1 and arr[nr][nc] not in (1, 2, 5, 6):
                        continue
                    if dc[d] == -1 and arr[nr][nc] not in (1, 3, 4, 5):
                        continue
                    queue.append((nr, nc))
                    visited[nr][nc] = visited[sr][sc] + 1
    

T = int(input())
for tc in range(1, T+1):
    N, M, r, c, t = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    bfs(r, c)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] >= 1:
                cnt += 1
    print(f'#{tc} {cnt}')
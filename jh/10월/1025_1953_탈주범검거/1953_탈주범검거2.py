from collections import deque

# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
opposite = [1, 0, 3, 2]

tunnel = [
    [],
    [0, 1, 2, 3],  # 1: 상하좌우
    [0, 1],        # 2: 상하
    [2, 3],        # 3: 좌우
    [0, 3],        # 4: 상우
    [1, 3],        # 5: 하우
    [1, 2],        # 6: 하좌
    [0, 2],        # 7: 상좌
]


def bfs(r, c):
    queue = deque([(r, c)])
    visited = [[0] * M for _ in range(N)]
    visited[r][c] = 1
    cnt = 1

    while queue:
        sr, sc = queue.popleft()

        if visited[sr][sc] >= t:
            break

        for d in tunnel[arr[sr][sc]]:
            nr, nc = sr + dr[d], sc + dc[d]

            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
                if opposite[d] in tunnel[arr[nr][nc]]:
                    visited[nr][nc] = visited[sr][sc] + 1
                    queue.append((nr, nc))
                    cnt += 1

    return cnt


T = int(input())
for tc in range(1, T + 1):
    N, M, r, c, t = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {bfs(r, c)}')
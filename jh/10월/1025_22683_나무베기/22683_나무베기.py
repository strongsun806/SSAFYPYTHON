from collections import deque


def bfs(sr, sc):
    # 행, 열, 방향, 나무를 벤 횟수
    visited = [
        [[[False] * (K + 1) for _ in range(4)] for _ in range(N)]
        for _ in range(N)
    ]

    # 행, 열, 방향, 나무를 벤 횟수, 조작 횟수
    queue = deque([(sr, sc, 0, 0, 0)])
    visited[sr][sc][0][0] = True

    while queue:
        r, c, direction, cut, cnt = queue.popleft()

        if field[r][c] == 'Y':
            return cnt

        # 1. 좌회전 또는 우회전
        for nd in [(direction - 1) % 4, (direction + 1) % 4]:
            if not visited[r][c][nd][cut]:
                visited[r][c][nd][cut] = True
                queue.append((r, c, nd, cut, cnt + 1))

        # 2. 현재 바라보는 방향으로 전진
        nr = r + dr[direction]
        nc = c + dc[direction]

        if 0 <= nr < N and 0 <= nc < N:
            next_cut = cut

            if field[nr][nc] == 'T':
                next_cut += 1

            if next_cut <= K and not visited[nr][nc][direction][next_cut]:
                visited[nr][nc][direction][next_cut] = True
                queue.append((nr, nc, direction, next_cut, cnt + 1))

    return -1


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    field = [list(input().strip()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if field[i][j] == 'X':
                sr, sc = i, j

    ans = bfs(sr, sc)
    print(f'#{tc} {ans}')
import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    tunnel = [[],[0, 1, 2, 3],[0, 1],[2, 3],[0, 3],[1, 3],[1, 2],[0, 2]]

    reverse = [1, 0, 3, 2]

    visited = [[0] * M for _ in range(N)]
    queue = [(R, C)]
    visited[R][C] = 1

    front = 0

    while front < len(queue):
        r, c = queue[front]
        front += 1
        if visited[r][c] == L:
            continue

        for d in tunnel[matrix[r][c]]:
            dr, dc = dir[d]
            nr = r + dr
            nc = c + dc
            if not (0 <= nr < N and 0 <= nc < M):
                continue

            if visited[nr][nc]:
                continue

            if matrix[nr][nc] == 0:
                continue

            if reverse[d] not in tunnel[matrix[nr][nc]]:
                continue

            visited[nr][nc] = visited[r][c] + 1
            queue.append((nr, nc))

    cnt = 0

    for r in range(N):
        for c in range(M):
            if visited[r][c]:
                cnt += 1

    print(f"#{tc} {cnt}")
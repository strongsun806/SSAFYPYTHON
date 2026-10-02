import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    test_case = int(input())
    matrix = [list(map(int, input())) for _ in range(16)]

    for r in range(16):
        for c in range(16):
            if matrix[r][c] == 2:
                sr = r
                sc = c

    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[0] * 16 for _ in range(16)]

    q = [(sr, sc)]
    visited[sr][sc] = 1

    front = 0
    result = 0
    while front < len(q):
        r, c = q[front]
        front += 1
        if matrix[r][c] == 3:
            result = 1
            break
        for dr, dc in dir:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < 16 and 0 <= nc < 16:
                if matrix[nr][nc] != 1 and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    q.append((nr, nc))

    print(f"#{test_case} {result}")
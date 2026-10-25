import sys
sys.stdin = open('input.txt', 'r')


def bfs(a, b):
    global ans
    queue = []
    queue.append((a, b))
    visited[a][b] = 1
    while queue:
        r, c = queue.pop(0)
        if maze[r][c] == 3:
            ans = 1
        for d in range(4):
            nr = r +dr[d]
            nc = c +dc[d]
            if 0 <= nr < 16 and 0 <= nc <16 and visited[nr][nc] == 0 and maze[nr][nc] != 1:
                visited[nr][nc] = 1
                queue.append((nr, nc))


T = 10
for tc in range(1, T+1):
    tc = input()
    maze = [list(map(int, input().strip())) for _ in range(16)]
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    visited = [[0]*16 for _ in range(16)]
    ans = 0
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                bfs(i, j)
                break
    print(f'#{tc} {ans}')

    
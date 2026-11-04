T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    max_flies = 0
    for r in range(N-M+1):
        for c in range(N-M+1):
            now_flies = 0
            for dr in range(M):
                for dc in range(M):
                    now_flies += grid[r+dr][c+dc]

            if now_flies > max_flies:
                max_flies = now_flies

    print(f"#{tc} {max_flies}")
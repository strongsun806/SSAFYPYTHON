dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    count = 0
    #전체 칸 순회하면서 나보다 낮은 곳에 가야지
    for r in range(N):
        for c in range(N):
            can_go_down = False
            # 4방향 델타 탐색

            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]

                #만약에 격자 내부에 있으면서 현재 칸 보다 낮은 곳이 있는지??
                if 0 <= nr < N and 0<= nc < N:
                    if grid[nr][nc] < grid[r][c]:
                        can_go_down = True
                        break #내리막이 한개라도 있으면 즉시 종료

            if can_go_down:
                count += 1


    print(f"#{tc} {count}")

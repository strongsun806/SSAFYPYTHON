import sys
# sys.stdin = open("input.txt", "r")

def drop_blocks(grid, W, H):
    # 중력 작용: 벽돌 아래로 떨어뜨리기
    for col in range(W):
        empty_row = H - 1
        for row in range(H - 1, -1, -1):
            if grid[row][col] != 0:
                val = grid[row][col]
                grid[row][col] = 0
                grid[empty_row][col] = val
                empty_row -= 1

def boom(start_r, start_c, grid, W, H):
    # 구슬이 맞은 벽돌 연쇄 폭발 (BFS/스택)
    stack = [(start_r, start_c, grid[start_r][start_c])]
    grid[start_r][start_c] = 0
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    while stack:
        r, c, power = stack.pop()
        for p in range(1, power):
            for k in range(4):
                nr = r + dr[k] * p
                nc = c + dc[k] * p
                if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] != 0:
                    stack.append((nr, nc, grid[nr][nc]))
                    grid[nr][nc] = 0

def dfs(depth, grid, N, W, H):
    global min_remain
    
    # 남은 벽돌 개수 세기
    remain = sum(row.count(0) for row in grid)
    total_blocks = W * H - remain
    
    if total_blocks == 0:
        min_remain = 0
        return
        
    if depth == N:
        if total_blocks < min_remain:
            min_remain = total_blocks
        return

    # W개의 열 중 하나를 선택해 구슬 투하
    for col in range(W):
        # 해당 열에서 가장 위에 있는 벽돌 찾기
        hit_row = -1
        for row in range(H):
            if grid[row][col] != 0:
                hit_row = row
                break
                
        # 벽돌이 없는 열은 패스
        if hit_row == -1:
            continue
            
        # 맵 복사 후 폭발 및 중력 처리
        new_grid = [r[:] for r in grid]
        boom(hit_row, col, new_grid, W, H)
        drop_blocks(new_grid, W, H)
        
        dfs(depth + 1, new_grid, N, W, H)
        
        if min_remain == 0:
            return

T = int(input())
for test_case in range(1, T + 1):
    N, W, H = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(H)]
    
    # 초기 벽돌 수 계산
    initial_blocks = sum(W - row.count(0) for row in matrix)
    min_remain = initial_blocks
    
    dfs(0, matrix, N, W, H)
    print(f"#{test_case} {min_remain}")

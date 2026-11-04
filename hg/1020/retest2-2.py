def dfs(r, c, path):
    # 기저 조건: 길이가 7이 되면 set에 추가하고 종료
    if len(path) == 7:
        result.add(path)
        return

    # 상하좌우 4방향 탐색
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        # 격자 범위 내에 있는지 확인
        if 0 <= nr < 4 and 0 <= nc < 4:
            dfs(nr, nc, path + grid[nr][nc])

T = int(input())
for tc in range(1, T + 1):
    grid = [list(input().split()) for _ in range(4)]
    result = set()  # 중복을 방지하기 위한 집합 자료형
    
    # 4x4 격자의 모든 칸을 시작점으로 하여 DFS 수행
    for i in range(4):
        for j in range(4):
            dfs(i, j, grid[i][j])
            
    print(f"#{tc} {len(result)}")
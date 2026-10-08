dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    
    grid = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    
    #Queue 기반 BFS (list & pointer 사용)
    queue = [(0, 0)]
    visited[0][0] = 1 # 시작 위치 방문 처리 (거리 1부터 시작)
    
    head = 0
    ans = -1
    
    while head < len(queue):
        r, c = queue[head]
        head += 1
        
        if r == N - 1 and c == N - 1:
            ans = visited[r][c]
            break
        
        for d in range(4):
            nr, nc = r+dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if grid[nr][nc] == 1 and visited[nr][nc] == 0:
                    visited[nr][nc] = visited[r][c] + 1
                    queue.append((nr, nc))
                    
    print(f"#{tc} {ans}")
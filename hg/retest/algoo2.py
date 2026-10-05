# 안전 내리막 산책로

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    
    #방문 기록 및 큐 초기화 ( 시작점 0, 0)
    visited = [[False]*N for _ in range(N)]
    queue = [(0,0)]
    visited[0][0] = True
    front = 0
    
    while front < len(queue):
        r, c = queue[front]
        front += 1
        
        #4방향 델타 탐색
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            
            # 격자 범위 내 검사
            if 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] < board[r][c] and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
                
                
    
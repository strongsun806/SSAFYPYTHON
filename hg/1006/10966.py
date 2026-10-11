# 10966 물놀이를 가자

#import sys
from collections import deque

# sys.stdin = open("input.txt", "r")
#input = sys.stdin.readline

# 상하좌우 탐색용
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [input().strip() for _ in range(N)]
    
    # 거리 배열: -1로 초기화 (방문 여부 겸용)
    dist = [[-1] * M for _ in range(N)]
    q = deque()
    
    # 1. 모든 물('W')의 위치를 큐에 넣고 거리 0으로 세팅
    for r in range(N):
        for c in range(M):
            if grid[r][c] == 'W':
                dist[r][c] = 0
                q.append((r, c))
                
    # 2. Multi-source BFS 탐색
    while q:
        r, c = q.popleft()
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            # 격자 범위 내이고 아직 방문하지 않은 칸인 경우
            if 0 <= nr < N and 0 <= nc < M and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
                
    # 3. 모든 칸까지의 최단 거리 합 계산
    total_dist = sum(sum(row) for row in dist)
    
    print(f"#{tc} {total_dist}")
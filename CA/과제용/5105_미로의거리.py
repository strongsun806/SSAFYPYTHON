import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    
    start = None
    end = None
    matrix = []
    
    # 미로 판떼기 입력 및 출발/도착점 찾기
    for i in range(N):
        row = list(map(int, input()))
        matrix.append(row)
        for j in range(N):
            if row[j] == 2:
                start = (i, j)
            elif row[j] == 3:
                end = (i, j)
                
    # 4방향 델타 탐색
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    # BFS 탐색용 큐와 거리 기록 배열
    queue = deque([start])
    visited = [[0] * N for _ in range(N)]
    visited[start[0]][start[1]] = 1
    
    distance = 0
    found = False
    
    while queue:
        r, c = queue.popleft()
        
        if (r, c) == end:
            # 출발지와 목적지 사이의 빈 칸 수 = 지나간 칸수 - 2
            distance = visited[r][c] - 2
            found = True
            break
            
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            
            if 0 <= nr < N and 0 <= nc < N:
                # 벽(1)이 아니고 아직 방문하지 않은 칸
                if matrix[nr][nc] != 1 and not visited[nr][nc]:
                    visited[nr][nc] = visited[r][c] + 1
                    queue.append((nr, nc))
                    
    if found:
        print(f"#{test_case} {distance}")
    else:
        print(f"#{test_case} 0")

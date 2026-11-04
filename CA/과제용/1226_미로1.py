import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

T = 10
for _ in range(T):
    test_case = int(input())
    
    matrix = []
    start = None
    end = None
    
    # 16x16 미로 판떼기 입력
    for i in range(16):
        row = list(map(int, input()))
        matrix.append(row)
        for j in range(16):
            if row[j] == 2:
                start = (i, j)
            elif row[j] == 3:
                end = (i, j)
                
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    visited = [[False] * 16 for _ in range(16)]
    queue = deque([start])
    visited[start[0]][start[1]] = True
    
    is_valid = 0
    while queue:
        r, c = queue.popleft()
        
        if (r, c) == end:
            is_valid = 1
            break
            
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            
            if 0 <= nr < 16 and 0 <= nc < 16:
                # 벽(1)이 아니고 미방문인 곳
                if matrix[nr][nc] != 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
                    
    print(f"#{test_case} {is_valid}")

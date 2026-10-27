T = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for t in range(1, T + 1):
    grid = [list(input().split()) for _ in range(4)]
    
    result_set = set()
    
    stack = []
    
    for i in range(4):
        for j in range(4):
            stack.append((i, j, grid[i][j]))
            
    while stack:
        x, y, current_str = stack.pop()
        
        if len(current_str) == 7:
            result_set.add(current_str)
            continue
            
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0 <= nx < 4 and 0 <= ny < 4:
                stack.append((nx, ny, current_str + grid[nx][ny]))
                
    # 결과 출력
    print(f"#{t} {len(result_set)}")
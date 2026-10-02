
def dfs(maze):
    # 시작점에서 목적지로 갈 수 있으면 1 반환 없으면 0 반환
    N=len(maze)
    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] ==2:
                sr=i
                sc=j
    #########################################
    stack=[]
    stack.append((sr,sc))
    # 미로와 동일한 모양의 visited 배열
    visited = [[0]*N for _ in range(N)]
    visited[sr][sc] = 1

    while stack:
        cr,cc = stack[-1]  #현재 위치
        if maze[cr][cc] ==3 :
            return 1
        # 현재위치에서 길찾기 >> 상하좌우 살피기
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr = cr+dr
            nc = cc+dc
            if 0<=nr<N and 0<=nc <N and maze[nr][nc] != 0 and visited[nr][nc]==0:
                stack.append((nr,nc))
                visited[nr][nc] = 1
                break
        else :   # 길 없으면 되돌아가라
            stack.pop()
    # 갈 수 있는 길 찾아봤는데 목적지가 없더라
    return 0

dfs(1)
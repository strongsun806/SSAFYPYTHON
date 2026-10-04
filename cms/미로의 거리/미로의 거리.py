import sys
sys.stdin = open("sample_input.txt","r")

T= int(input())
for tc in range(1, T+1):
    N = int(input())
    maze=[list(map(int, input().strip())) for _ in range(N)]

    start = None
    goal = None
    for i in range(N):
        for j in range(N):
            if maze[i][j]==2:
                start = (i,j)
            if maze[i][j]==3:
                goal = (i,j)


    dr=[0,0,1,-1]
    dc=[1,-1,0,0]

    visited=[[0]*N for _ in range(N)]

    r,c= start[0], start[1]
    visited[r][c] = 1

    q=[]
    q.append(start)

    cnt = -1

    while q :
        cnt +=1
        for _ in range(len(q)):
            r,c = q.pop(0)
            for i in range(4):
                nr = r+dr[i]
                nc = c+dc[i]
                if 0<=nr<N and 0<=nc<N :
                    if maze[nr][nc] ==3 :
                        visited[nr][nc]=1
                        break
                    elif maze[nr][nc] == 0 and visited[nr][nc]==0:
                        visited[nr][nc]=1
                        q.append((nr,nc))
            if visited[goal[0]][goal[1]]==1:
                break
        if visited[goal[0]][goal[1]]==1:
            break

    if visited[goal[0]][goal[1]]==0:
        cnt = 0

    print(f"#{tc} {cnt}")

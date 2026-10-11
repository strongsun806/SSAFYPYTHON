#2차원 행렬에서 dfs
# 전에는 그래프 표현으로 인접행렬을 사용
# 연결 정보를 인접행렬을 리용해서 확인

# 2차원 행렬 >> 연결 정보를 확인할 필요도 없음 어차피 상하좌우 연결이니까
# 4개만 보면 된다. 델타만 하면 됨
# 정점 하나를 좌표로 표현 (r, c) 나랑 인접한 정점은 (r-1, c), (), (), ()
#0: 벽, 1: 통로, 2: 시작점, 3: 도착점

maze1 = [
    [0,1,0,0,0],
    [1,2,1,1,1],
    [0,0,0,1,0],
    [0,1,0,1,0],
    [3,1,1,1,0]
]
# 목적지에 도착할 수 있는지 여부 출력

maze2 = [
    [0,1,0,0,0],
    [1,2,1,1,1],
    [0,0,0,1,0],
    [0,1,0,0,0],
    [3,1,1,1,0]
]

def dfs(maze):
    # 시작점에서 목적지로 갈 수 있으면 1 반환, 없으면 0 반환
    N = len(maze)


    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sr = i
                sc = j
    ##############################
    stack = []
    # stack.append(시작정점)
    stack.append((sr, sc))
    # 미로와 동일한 모양의 visited 배열을 만들거임
    visited = [[0] * N for _ in range(N)]
    visited[sr][sc] = 1

    while stack:

        # current =  stack[-1]
        cr, cc = stack[-1]  # 현재 위치
        if maze[cr][cc] == 3:
            return 1

        # 현재 위치에서 길 찾기 >> 상하좌우 살피기
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            # 다음에 봐야할 좌표
            nr = cr + dr
            nc = cc + dc
            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != 0 and visited[nr][nc] == 0:
            #          정상범위이면서               0이 아니라면             방문도 안했다면
                stack.append((nr, nc))
                visited[nr][nc] = 1
                break
        else:  # 길 없으면 돌아가라
            stack.pop()

    # 여기까지 온거면 길을 모두 찾아봤지만 못찾은거임(retrun 1이 안된거임)ㅠㅠ
    return 0

print(dfs(maze1))
print(dfs(maze2))
import sys
sys.stdin = open('sample_input.txt', 'r')

# 델타
d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
# dfs(행, 열, 공사 가능 여부, 이동거리) / sr,sc : 시작 지점 / kr,kc : 공사 위치
def dfs(r, c):
    global max_length, l, k
    l += 1
    visited[r][c] = 1
    for dr, dc in d:    # 현재 정점에서 갈 수 있는 길 찾기....
        nr = r + dr
        nc = c + dc
        # 공사 가능여부 확인
        if k > 0:
            # 이동 할 곳이 정상범위 이며, 방문하지 않았으며, 공사 후에 현재 위치보다 낮은지 확인
            if 0<= nr < N and 0<=nc<N and visited[nr][nc] == 0 and (mountain[nr][nc]-k) < mountain[r][c]:
                # 공사를 해야 하는지 확인, 공사를 해야한다면 공사후 k는 0으로 바꿈
                if mountain[nr][nc] >= mountain[r][c]:
                    kn = 0
                    recover = mountain[nr][nc]
                    while mountain[nr][nc] >= mountain[r][c] and mountain[nr][nc] > 0 and kn < K:
                        mountain[nr][nc] -= 1
                        kn += 1
                    k = 0
                    dfs(nr, nc)
                    k = K
                    mountain[nr][nc] = recover
                    visited[nr][nc] = 0
                else:
                    dfs(nr, nc)
                    visited[nr][nc] = 0
        else:
            # 공사를 이미 했다면 이동위치가 현재 위치보다 낮아야함
            if 0<= nr < N and 0<=nc<N and visited[nr][nc] == 0 and mountain[nr][nc] < mountain[r][c]:
                    dfs(nr, nc)
                    visited[nr][nc] = 0

    # 이동거리가 최대라면 저장
    if l > max_length:
        max_length = l
    l -= 1

        
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    max_length = 0
    highest = 0
    # 경로 스택, 방문 체크, 최대길이
    visited = [[0]*N for _ in range(N)]
    l = 0
    k = K
    # 최대 높이 찾기
    for i in range(N):
        for j in range(N):
            if mountain[i][j] > highest:
                highest = mountain[i][j]
    # 최대 높이에서 dfs
    for i in range(N):
        for j in range(N):
            if mountain[i][j] == highest:
                dfs(i, j)
                visited[i][j] = 0

    print(f'#{tc} {max_length}')
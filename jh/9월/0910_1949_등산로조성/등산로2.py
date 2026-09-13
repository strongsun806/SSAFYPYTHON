import sys

sys.stdin = open('sample_input.txt', 'r')

# 델타
d = [(0, 1), (1, 0), (-1, 0), (0, -1)]


# dfs(행, 열, 공사 가능 여부, 이동거리) / sr,sc : 시작 지점 / kr,kc : 공사 위치
def dfs(r, c):
    global max_length
    k = K
    sr = r
    sc = c
    kr = 0
    kc = 0
    l = 1
    stack = []
    visited = [[0] * N for _ in range(N)]
    stack.append([sr, sc,0,visited])
    visited[sr][sc] = 1
    while stack:
        cr, cc, d = stack.pop()
        for i in range(d,4):  # 현재 정점에서 갈 수 있는 길 찾기....
            nr = cr + d[i][0]
            nc = cc + d[i][1]
            # 공사 가능여부 확인
            if k > 0:
                # 이동 할 곳이 정상범위 이며, 방문하지 않았으며, 공사 후에 현재 위치보다 낮은지 확인
                if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and (mountain[nr][nc] - k) < mountain[cr][cc]:
                    # 공사를 해야 하는지 확인, 공사를 해야한다면 공사후 k는 0으로 바꿈
                    if mountain[nr][nc] >= mountain[cr][cc]:
                        mountain[nr][nc] -= k
                        k = 0
                        kr = nr
                        kc = nc
                        stack.append(cr,cc,d+1)
                        stack.append((nr, nc))
                        visited[nr][nc] = 1
                        l += 1
                        break  # for dr, dc in d:
                    else:
                        stack.append((nr, nc))
                        visited[nr][nc] = 1
                        l += 1
                        break  # for dr, dc in d:

            else:
                # 공사를 이미 했다면 이동위치가 현재 위치보다 낮아야함
                if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and mountain[nr][nc] < mountain[cr][cc]:
                    stack.append((nr, nc))
                    visited[nr][nc] = 1
                    l += 1
                    break  # for dr, dc in d:
        # 더이상 갈곳이 없음.
        else:
            pr, pc = stack.pop()
            if pr == kr and pc == kc:
                k = K
                mountain[pr][pc] += k
            # 이동거리가 최대라면 저장
            if l > max_length:
                max_length = l
            l -= 1


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    stack = []
    visited = [[0] * N for _ in range(N)]
    max_length = 0
    highest = 0
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

    print(f'#{tc} {max_length}')

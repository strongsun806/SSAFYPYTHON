import sys
sys.stdin = open('sample_input.txt', 'r')

from collections import deque

def bfs(r, c):
    global ans
    queue = deque()
    visited = [0]*(N+1)
    visited[r] = 1
    visited[c] = 1
    queue.append((r, c, 2, visited))
    while queue:
        s, e, cnt, visit = queue.popleft()
        ans = max(ans, cnt)
        for i in range(N+1):    
            if node[e][i] == 1 and visit[i] == 0:
                next_visit = visit[:]
                next_visit[i] = 1
                queue.append((e, i, cnt + 1, next_visit))
    

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    edge = []
    node = [[0] * (N+1) for _ in range(N+1)]
    ans = 1
    for _ in range(M):
        s, e = map(int, input().split())
        edge.append((s, e))
    for a, b in edge:
        node[a][b] = 1
        node[b][a] = 1

    for i in range(1, N+1):
        for j in range(1, N+1):
            if node[i][j] == 1:
                bfs(i, j)
    print(f'#{tc} {ans}')
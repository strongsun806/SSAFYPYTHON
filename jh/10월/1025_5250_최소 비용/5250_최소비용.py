import sys
sys.stdin = open('sample_input.txt')

import heapq

def dijkstra(r, c):
    dist[r][c] = 0
    dr = [-1,1,0,0]
    dc = [0,0,1,-1]
    heap = [(0, r, c)]
    while heap:
        cost, sr, sc = heapq.heappop(heap)
        if cost > dist[sr][sc]:
            continue
        for d in range(4):
            nr = sr + dr[d]
            nc = sc + dc[d]
            if 0<= nr < N and 0 <= nc < N:
                if arr[sr][sc] < arr[nr][nc]:
                    new_cost = cost + arr[nr][nc] - arr[sr][sc] + 1
                else:
                    new_cost = cost + 1
                if new_cost < dist[nr][nc]:
                    dist[nr][nc] = new_cost
                    heapq.heappush(heap, (new_cost, nr, nc))
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dist = [[float('inf')]*(N) for _ in range(N)]
    dijkstra(0, 0)
    print(f'#{tc} {dist[N-1][N-1]}')
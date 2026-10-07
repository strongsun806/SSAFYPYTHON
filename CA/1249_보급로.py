import heapq
# sys.stdin = open("input.txt", "r")

# 4방향 델타 탐색 (상, 하, 좌, 우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 공백 없는 문자열 행렬 입력
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, list(input().strip()))))
        
    dist = [[float('inf')] * N for _ in range(N)]
    dist[0][0] = 0
    heap = [(0, 0, 0)]  # (누적 복구 시간, r, c)
    
    while heap:
        cur_cost, r, c = heapq.heappop(heap)
        
        # 도착지에 도달하면 최단 비용 확정
        if (r, c) == (N - 1, N - 1):
            break
            
        if dist[r][c] < cur_cost:
            continue
            
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            
            if 0 <= nr < N and 0 <= nc < N:
                nxt_cost = cur_cost + matrix[nr][nc]
                if nxt_cost < dist[nr][nc]:
                    dist[nr][nc] = nxt_cost
                    heapq.heappush(heap, (nxt_cost, nr, nc))
                    
    print(f"#{tc} {dist[N - 1][N - 1]}")

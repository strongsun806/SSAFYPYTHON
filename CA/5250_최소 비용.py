import heapq
# sys.stdin = open("input.txt", "r")

# 4방향 델타 탐색 (상, 하, 좌, 우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
        
    dist = [[float('inf')] * N for _ in range(N)]
    dist[0][0] = 0
    heap = [(0, 0, 0)]  # (소비 연료, r, c)
    
    while heap:
        cur_fuel, r, c = heapq.heappop(heap)
        
        if (r, c) == (N - 1, N - 1):
            break
            
        if dist[r][c] < cur_fuel:
            continue
            
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            
            if 0 <= nr < N and 0 <= nc < N:
                # 기본 이동 비용 1 + 높이 차이에 따른 추가 비용
                diff = max(0, matrix[nr][nc] - matrix[r][c])
                nxt_fuel = cur_fuel + 1 + diff
                
                if nxt_fuel < dist[nr][nc]:
                    dist[nr][nc] = nxt_fuel
                    heapq.heappush(heap, (nxt_fuel, nr, nc))
                    
    print(f"#{tc} {dist[N - 1][N - 1]}")

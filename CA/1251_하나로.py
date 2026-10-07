import heapq
# sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    
    # 프림 알고리즘 (밀집 그래프 최적화)
    visited = [False] * N
    min_cost = [float('inf')] * N
    min_cost[0] = 0
    heap = [(0, 0)]  # (거리의 제곱, 섬 인덱스)
    
    total_dist_sq = 0
    cnt = 0
    
    while heap:
        cur_d, u = heapq.heappop(heap)
        
        if visited[u]:
            continue
            
        visited[u] = True
        total_dist_sq += cur_d
        cnt += 1
        
        if cnt == N:
            break
            
        for v in range(N):
            if not visited[v]:
                dist_sq = (X[u] - X[v]) ** 2 + (Y[u] - Y[v]) ** 2
                if dist_sq < min_cost[v]:
                    min_cost[v] = dist_sq
                    heapq.heappush(heap, (dist_sq, v))
                    
    # 환경 부담 세율 E를 곱한 후 반올림
    ans = round(E * total_dist_sq)
    print(f"#{tc} {ans}")

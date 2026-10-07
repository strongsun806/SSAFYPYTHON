import heapq
# sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))
        
    # 다익스트라 최단 거리
    dist = [float('inf')] * (N + 1)
    dist[0] = 0
    heap = [(0, 0)]  # (누적거리, 현재노드)
    
    while heap:
        cur_d, u = heapq.heappop(heap)
        
        if dist[u] < cur_d:
            continue
            
        for v, w in graph[u]:
            nxt_d = cur_d + w
            if nxt_d < dist[v]:
                dist[v] = nxt_d
                heapq.heappush(heap, (nxt_d, v))
                
    print(f"#{tc} {dist[N]}")

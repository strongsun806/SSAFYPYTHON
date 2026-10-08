# sys.stdin = open("input.txt", "r")

def dfs(now):
    global count
    # 도착점 G에 도달하면 경로 1개 완성
    if now == G:
        count += 1
        return
        
    for nxt in graph[now]:
        # 현재 경로에서 아직 방문하지 않은 정점만 이동
        if not visited[nxt]:
            visited[nxt] = 1   # 방문 표시
            dfs(nxt)
            visited[nxt] = 0   # 다른 경로 탐색을 위해 원상복구 (백트래킹)

T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    
    # 간선 정보 받기 (한 줄 입력 또는 E개 줄 입력 모두 처리)
    edges = []
    while len(edges) < 2 * E:
        edges.extend(map(int, input().split()))
        
    for i in range(0, len(edges), 2):
        u = edges[i]
        v = edges[i + 1]
        graph[u].append(v)
        
    S, G = map(int, input().split())
    
    visited = [0] * (N + 1)
    visited[S] = 1   # 시작점 방문 체크
    count = 0
    
    dfs(S)
    
    print(f"#{tc} {count}")

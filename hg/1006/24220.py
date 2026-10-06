#import sys

# sys.stdin = open("input.txt", "r")

def dfs(current, target):
    global ans
    
    # 목적지에 도달했다면?
    if current == target:
        ans += 1
        return

    for nxt in adj[current]:
        if not visited[nxt]:
            visited[nxt] = True
            dfs(nxt, target)
            visited[nxt] = False  # 백트래킹 (원상복구)


T = int(input())
for tc in range(1, T + 1):
    # N: 정점의 수, E: 간선의 수
    N, E = map(int, input().split())
    
    adj = [[] for _ in range(N + 1)]
    
    # 간선 정보 입력
    edges = list(map(int, input().split()))
    for i in range(0, len(edges), 2):
        u, v = edges[i], edges[i + 1]
        adj[u].append(v)
        
    start, end = map(int, input().split())
    
    visited = [False] * (N + 1)
    ans = 0
    
    visited[start] = True
    dfs(start, end)
    
    print(f"#{tc} {ans}")
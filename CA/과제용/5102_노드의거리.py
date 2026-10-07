import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    
    # 인접 리스트로 그래프 구성
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        start_node, end_node = map(int, input().split())
        graph[start_node].append(end_node)
        graph[end_node].append(start_node)
        
    S, G = map(int, input().split())
    
    # BFS로 최단 거리 탐색
    visited = [0] * (V + 1)
    queue = deque([S])
    visited[S] = 1 # 시작 위치 방문 처리 (거리 계산 시 -1 해줌)
    
    found = False
    while queue:
        cur = queue.popleft()
        
        if cur == G:
            found = True
            break
            
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = visited[cur] + 1
                queue.append(nxt)
                
    if found:
        print(f"#{test_case} {visited[G] - 1}")
    else:
        print(f"#{test_case} 0")

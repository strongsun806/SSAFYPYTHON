# ========================================================
# 문제: 1219_[S/W 문제해결 기본] 4일차 - 길찾기
# 난이도: D4
# 작성자: 윤형섭 (1627575)
# 제출 결과: Pass
# 저장 일시: 2026-10-07 11:35:29
# ========================================================

def dfs(current, target, graph, visited):
    if current == target:
        return 1
         visited[current] = True
    for nxt in graph[current]:
        if nxt is not None and not visited[nxt]:
            if dfs(nxt, target, graph, visited):
                return 1
    return 0
 T = 10
for _ in range(T):
    tc, n = map(int, input().split())
    edges = list(map(int, input().split()))
         graph = [[None, None] for _ in range(100)]
    for i in range(0, n * 2, 2):
        a, b = edges[i], edges[i + 1]
        if graph[a][0] is None:
            graph[a][0] = b
        else:
            graph[a][1] = b
                 visited = [False] * 100
    answer = dfs(0, 99, graph, visited)
    print(f"#{tc} {answer}")

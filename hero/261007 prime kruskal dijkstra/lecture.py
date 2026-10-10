import sys

# import heapq


# def prim(graph, start):
#     # graph[u] = [(가중치, 연결정점), ...]
    
#     visited = [False] * len(graph)

#     # 우선순위 큐
#     # (가중치, 현재 정점, 부모 정점)
#     pq = [(0, start, -1)]

#     total_weight = 0
#     mst = []

#     while pq:
#         weight, u, parent = heapq.heappop(pq)

#         # 이미 MST에 포함된 정점이면 무시
#         if visited[u]:
#             continue

#         # MST에 포함
#         visited[u] = True
#         total_weight += weight

#         # 시작 정점이 아니면 간선 저장
#         if parent != -1:
#             mst.append((parent, u, weight))

#         # u와 연결된 정점 확인
#         for next_weight, v in graph[u]:
#             if not visited[v]:
#                 heapq.heappush(pq, (next_weight, v, u))

#     return total_weight, mst


##########################################
# Prim 알고리즘
sys.stdin = open("input_prime.txt", "r")
import heapq


def prim(graph, start, V):
    INF = float('inf')

    # 각 정점을 어떤 간선으로 MST에 붙일지 기억하는 용도
    key = [INF] * (V + 1)  # key[v] == v번 정점을 MST에 붙일 때 지금까지 발견한 가장 싼 비용
    parent = [None] * (V + 1)  # parent[v] == 그 가장 싼 비용으로 v번 정점을 연결해주는 부모 정점

    visited = [False] * (V + 1)

    # 실제 MST 간선 저장
    mst = []

    # 시작 정점은 비용 0
    key[start] = 0

    # (비용, 정점)
    pq = []  # pq: priority queue == 우선순위 큐
    heapq.heappush(pq, (0, start))

    while pq:
        current_key, u = heapq.heappop(pq)

        # 이미 MST에 들어간 정점이면 넘어감
        if visited[u]:
            continue

        # MST에 포함
        visited[u] = True

        # 시작 정점이 아니면
        # parent[u] - u가 최종 선택된 간선
        if parent[u] is not None:
            mst.append((parent[u], u, current_key))

        # u와 연결된 정점들 확인
        for v, weight in graph[u]:

            # 아직 MST에 안 들어갔고
            # 지금 간선이 기존 후보보다 더 싸다면
            if not visited[v] and weight < key[v]:

                key[v] = weight
                parent[v] = u

                heapq.heappush(pq, (key[v], v))

    return key, parent, mst

    # key
    # # [inf, 0, 2, 1, 4]

    # parent
    # # [None, None, 1, 2, 2]

    # mst
    # # [(1, 2, 2), (2, 3, 1), (2, 4, 4)]

V, E = map(int, input().split())

edges = []

for i in range(E):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))
    

# V = 4  # 정점의 개수

graph = [[] for _ in range(V + 1)]  # 노드 번호를 1번 부터 쓰기 위해
                                    # but visited로 쓰려는건 아님 ㅇㅇ
                                    # 다만 visited도 이렇게 따로 만들어줌

edges = [
    (1, 2, 2),
    (1, 3, 3),
    (2, 3, 1),
    (2, 4, 4),
    (3, 4, 5)
]

for u, v, w in edges:
    graph[u].append((v, w))
    graph[v].append((u, w))
    # 무방향 그래프라서 양쪽 정보를 다 넣어줌

    # graph[0] = []

    # graph[1] = [(2, 2), (3, 3)]

    # graph[2] = [(1, 2), (3, 1), (4, 4)]

    # graph[3] = [(1, 3), (2, 1), (4, 5)]

    # graph[4] = [(2, 4), (3, 5)]

print(prim(graph, 1, V))
print()
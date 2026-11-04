import sys
sys.stdin = open("D3_5250. [파이썬 SW 문제해결 구현] 7일차 - 최소 비용/input.txt", "r")

import heapq


def dijkstra(graph, start, V):
    INF = float('inf')

    # 시작점에서 각 정점까지의 최소 누적 거리
    distance = [INF] * (V + 1)

    # 시작점에서 시작점까지의 거리는 0
    distance[start] = 0

    # 우선순위 큐
    # (누적 거리, 정점 번호)
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:

        # 현재까지 누적 거리가 가장 작은 정점 꺼내기
        current_dist, n1 = heapq.heappop(pq)

        # 이미 더 짧은 경로를 발견했다면 무시
        if current_dist > distance[n1]:
            continue

        # 현재 정점과 연결된 정점 확인
        for n2, weight in graph[n1]:

            # n1을 거쳐 n2까지 이동했을 때의 누적 거리
            new_dist = current_dist + weight

            # 기존 거리보다 짧다면 갱신
            if new_dist < distance[n2]:

                distance[n2] = new_dist

                heapq.heappush(pq, (new_dist, n2))

    return distance

V = 4

edges = [
    (1, 2, 2),
    (1, 3, 5),
    (2, 3, 1),
    (2, 4, 4),
    (3, 4, 2)
]

graph = [[] for _ in range(V + 1)]

for n1, n2, w in edges:
    graph[n1].append((n2, w))
    graph[n2].append((n1, w))

distance = dijkstra(graph, 1, V)

print(distance)  # [inf, 0, 2, 3, 5]
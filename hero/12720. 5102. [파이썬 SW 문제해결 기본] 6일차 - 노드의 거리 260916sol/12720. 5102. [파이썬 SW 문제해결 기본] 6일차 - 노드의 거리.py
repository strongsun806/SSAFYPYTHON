import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())  # V: 노드 개수, E: 방향성이 없는 E개의 간선 정보

    list_edges = []
    for i in range(E):
        list_edges.append(list(map(int, input().split())))

    S, G = map(int, input().split())  # S: 출발 노드, G: 도착 노드

    matrix_edge = []
    for i in range(V + 1):
        row = []
        for j in range(V + 1):
            row.append(0)
        matrix_edge.append(row)

    # matrix_edge에 간선 정보 입히기
    for edge in list_edges:
        i, j = edge
        matrix_edge[i][j] = 1
        matrix_edge[j][i] = 1

    # def bfs_node(Graph, Start_point):     # Graph: 그래프, Start_point: 탐색 시작점
    #     visited = [0] * (V + 1)           # V: 정점(노드)의 개수
    #     queue = []                        # queue 생성
    #     queue.append(Start_point)         # 탐색 시작점을 queue에 삽입
    #     while queue:                      # queue가 비어있지 않은 경우
    #         t = queue.pop(0)              # queue의 첫번째 원소 pop하기
    #         if not visited[t]:            # 방문하지 않은 곳이면
    #             visited[t] = True         # 방문한 것으로 표시
    #             visit(t)                  # 정점(노드) t에서 할 일
    #             for i in Graph[t]:        # t와 연결된 모든 정점(노드)에 대해
    #                 if not visited[i]:    # 방문하지 않은 곳이면
    #                     queue.append(i)   # queue에 넣기

    def bfs_node(Graph, Start_point):       # Graph: 그래프, Start_point: 탐색 시작점
        visited = [0] * (V + 1)             # V: 정점(노드)의 개수
        queue = []                          # queue 생성

        queue.append(Start_point)           # 탐색 시작점을 queue에 삽입
        visited[Start_point] = 1            # queue에 넣는 순간 방문처리

        while queue:                        # queue가 비어있지 않은 경우
            tmp = queue.pop(0)              # queue의 첫번째 원소 pop하기


            for a in range(1, V + 1):   # 정점(노드) t에서 할 일
                if Graph[tmp][a] == 1 and not visited[a]:
                    queue.append(a)
                    visited[a] = 1          # queue에 넣는 순간 방문처리



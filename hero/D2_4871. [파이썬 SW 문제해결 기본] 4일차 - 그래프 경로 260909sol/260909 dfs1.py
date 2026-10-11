V, E = map(int, input().split())
edges = list(map(int, input().split()))
# 인접행렬로 변환
adj = [[0] * (V+1) for _ in range(V+1)]

# edges가 연결정보니까 2개씩 끊어서 읽기
for i in range(0, E*2, 2):
    # edges[i]번과, edges[i+1]번 정점이 연결되어 있음
    s = edges[i]
    e = edges[i+1]
    adj[s][e] = 1
    adj[e][s] = 1


    # 그래프의 모든 정점을 순회하기
    # 일단 경로를 찾으면 해당 경로로 이동하고
    # 경로가 없으면 이전 정점으로 되돌아가서 다시 길찾기

    # 현재 지점과 연결된 지점 찾기
    # adj[3] << 이 행이 3번 정점과 연결된 정보
    # i번 열에 값이 1이라면, 3번과 i번은 연결된 것
    # 되돌아가서 길찾기 : stack에 방문한 정점을 저장하고 마지막 방문 정점을 지우면
    # 이전 정점으로 되돌아가는 것과 의미적으로 같다

    def dfs(start):
        stack = []
        stack.append(start)

        visited = [0] * (V + 1)
        visited[start] = 1  # 시작 지점 방문 처리

        # 경로가 
        while stack:
        # while len(stack) > 0:
            # 현재 위치에서 갈 수 있는 길 찾아보기
            # 현재위치: 경로상 마지막 정점
            current = stack[-1]

            # 인접행렬 adj[current] 살펴보기
            for v in range(1, V + 1):  # v: current와 인접한지 확인하려는 정점 번호
                if adj[current][v] and visited[v] == 0:
                # 또는 if adj[current][v] and not visited[v]:
                # v정점이 current와 인접하며, 아직 방문하지 않았다면 방문
                    stack.append(v)
                    visited[v] = 1
                    break  # 이동 가능한 경로 찾았으니 길 찾는거 멈추고 이동
                           # if문 안에서 길을 찾았을 때 break하는거임

                # 길을 못찾았다면?
                else:  # current 에서 이동가능한 정점이 없을 경우!
                    stack.pop()  # 현재 정점을 경로(stack)에서 제거, 이전 정점으로 이동
            print('DFS끝')

    dfs(1)

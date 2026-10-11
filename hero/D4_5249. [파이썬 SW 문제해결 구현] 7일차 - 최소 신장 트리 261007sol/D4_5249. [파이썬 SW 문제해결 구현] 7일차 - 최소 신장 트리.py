import sys
sys.stdin = open("5249. [파이썬 SW 문제해결 구현] 7일차 - 최소 신장 트리/input.txt", "r")
# Prim 알고리즘으로 풀이함
import heapq  # 우선순위 큐(최소 힙)를 사용하기 위한 라이브러리


# Prim 알고리즘: 최소 신장 트리(MST)를 구하는 함수
def prim(graph, start, V):
    # graph: 각 정점과 연결된 정점 및 가중치 정보가 저장된 인접 리스트
    # start: Prim 알고리즘을 시작할 정점 번호
    # V: 마지막 정점 번호 (정점은 0 ~ V, 총 V+1개)

    INF = float('inf')  # 무한대 값

    # key[v]
    # 현재 MST와 v번 정점을 연결할 수 있는 간선 중
    # 지금까지 발견한 가장 작은 가중치
    # 처음에는 연결 정보를 모르므로 모두 무한대로 초기화
    key = [INF] * (V + 1)

    # parent[v]
    # v번 정점을 MST에 연결할 때 사용하는 부모 정점 번호
    # 처음에는 연결된 부모가 없으므로 None으로 초기화
    parent = [None] * (V + 1)

    # visited[v]
    # v번 정점이 MST에 최종적으로 포함되었는지 확인
    # False: 아직 MST에 포함되지 않음
    # True: 이미 MST에 포함됨
    visited = [False] * (V + 1)

    # MST에 최종적으로 선택된 간선들을 저장할 리스트
    # (부모 정점, 현재 정점, 가중치) 형태로 저장
    mst = []

    # 시작 정점은 다른 정점과 연결되어 들어오는 것이 아니므로
    # 연결 비용을 0으로 설정
    key[start] = 0

    # pq: Priority Queue(우선순위 큐)
    # 현재 MST에 연결할 수 있는 정점 후보들을 관리
    # (가중치, 정점 번호) 형태로 저장
    # heapq를 사용하면 가중치가 가장 작은 후보부터 꺼낼 수 있음
    pq = []

    # 시작 정점을 우선순위 큐에 삽입
    # 시작 정점은 연결 비용이 0
    heapq.heappush(pq, (0, start))

    # 우선순위 큐에 확인할 후보가 남아 있는 동안 반복
    while pq:

        # 현재 후보 중 가중치가 가장 작은 정점을 꺼냄
        # current_key: 해당 후보의 연결 가중치
        # n1: 현재 확인할 정점 번호
        current_key, n1 = heapq.heappop(pq)

        # 이미 MST에 포함된 정점이라면 다시 처리할 필요 없음
        # heapq에는 같은 정점이 여러 번 들어갈 수 있기 때문
        if visited[n1]:
            continue

        # n1번 정점을 MST에 최종적으로 포함
        visited[n1] = True

        # 시작 정점은 부모가 없으므로 간선을 저장하지 않음
        # 나머지 정점은 자신을 MST에 연결한 간선을 저장
        if parent[n1] is not None:

            # (부모 정점, 현재 정점, 가중치)
            mst.append((parent[n1], n1, current_key))

        # 현재 MST에 새로 포함된 n1과 연결된 정점들을 확인
        # graph[n1]에는 (연결된 정점, 가중치) 형태의 정보가 저장됨
        for n2, weight in graph[n1]:

            # n2: n1과 연결된 정점 번호
            # weight: n1과 n2를 연결하는 간선의 가중치

            # 조건 1: n2가 아직 MST에 포함되지 않았는가?
            # 조건 2: 지금 발견한 간선의 가중치가
            #         기존에 알고 있던 key[n2]보다 작은가?
            if not visited[n2] and weight < key[n2]:

                # n2를 더 저렴하게 연결할 방법을 발견했으므로
                # n2의 최소 연결 비용을 갱신
                key[n2] = weight

                # n2를 n1을 통해 연결하는 것이 더 저렴하므로
                # n2의 부모를 n1로 변경
                parent[n2] = n1

                # 갱신된 연결 비용과 정점을 우선순위 큐에 추가
                # 이후 가장 작은 가중치를 가진 후보부터 처리됨
                heapq.heappush(pq, (key[n2], n2))

    # 모든 정점이 MST에 포함되었다면
    # key에는 각 정점을 MST에 연결하는 데 선택된 간선의 가중치가 저장됨

    # MST 전체 가중치 합계 계산
    answer = 0

    for i in range(len(key)):
        answer += key[i]

    # 최소 신장 트리의 전체 가중치 반환
    return answer


# ==========================================================
# 입력 및 그래프 생성
# ==========================================================

# 테스트케이스 개수
T = int(input())

for tc in range(1, T + 1):

    # V: 마지막 정점 번호
    #    실제 정점 번호는 0 ~ V이므로 총 V+1개
    # E: 간선의 개수
    V, E = map(int, input().split())

    # 입력받은 간선 정보를 저장할 리스트
    # 각 간선은 (정점1, 정점2, 가중치) 형태
    edges = []

    # E개의 간선 정보 입력받기
    for i in range(E):

        # n1: 첫 번째 정점
        # n2: 두 번째 정점
        # w: 두 정점 사이의 가중치
        n1, n2, w = map(int, input().split())

        # 간선 정보 저장
        edges.append((n1, n2, w))

    # 인접 리스트 생성
    # 정점 번호가 0 ~ V이므로 V+1개의 빈 리스트 생성
    #
    # graph[0] -> 0번 정점과 연결된 정보
    # graph[1] -> 1번 정점과 연결된 정보
    # ...
    # graph[V] -> V번 정점과 연결된 정보
    graph = [[] for _ in range(V + 1)]

    # 입력받은 간선 정보를 인접 리스트에 저장
    for n1, n2, w in edges:

        # n1에서 n2로 가는 간선 정보 저장
        graph[n1].append((n2, w))

        # n2에서 n1로 가는 간선 정보 저장
        graph[n2].append((n1, w))

        # 무방향 그래프이므로 양쪽 정점에 모두 저장
        # 실제 간선 하나를 인접 리스트에 두 번 기록하는 것

    # Prim 알고리즘 실행
    # graph: 전체 그래프 정보
    # 0: 시작 정점 번호
    # V: 마지막 정점 번호
    #
    # 반환값: MST의 전체 가중치
    print(f'#{tc} {prim(graph, 0, V)}')
import sys
sys.stdin = open("D3_24220. 경로의 수/input.txt", "r")

T = int(input())

for tc in range(1, T + 1):

    # N: 정점(Node)의 개수
    # E: 간선(Edge)의 개수
    N, E = map(int, input().split())


    # 인접 리스트 생성
    # 정점 번호를 1번부터 사용하기 위해 N + 1개 생성
    #
    # 예)
    # matrix[1] = [2, 3]
    # -> 1번 정점에서 2번, 3번 정점으로 갈 수 있다는 뜻
    matrix = []

    for i in range(N + 1):
        matrix.append([])


    # 간선 정보를 한 줄로 입력받기
    #
    # 예)
    # 1 2 1 3 2 4
    #
    # -> 1 -> 2
    # -> 1 -> 3
    # -> 2 -> 4
    list_tmp = list(map(int, input().split()))


    # 간선 정보는
    # [시작 정점, 도착 정점] 순서로 2개씩 묶여 있음
    for i in range(len(list_tmp)):

        # 짝수 번째 인덱스에서만
        # 시작 정점과 도착 정점을 묶어서 처리
        if i % 2 == 0:
            start = list_tmp[i]
            end = list_tmp[i + 1]

            # start 정점에서 end 정점으로 이동 가능
            matrix[start].append(end)


    # S: 출발 정점
    # G: 도착 정점
    S, G = map(int, input().split())


    # 각 정점을 현재 경로에서 방문했는지 체크
    #
    # used[i] == 1
    # -> 현재 탐색 경로에서 i번 정점을 이미 방문함
    used = [0] * (N + 1)


    # S에서 G까지 갈 수 있는 경로의 개수
    cnt = 0


    def dfs_24220(node_now):
        global cnt

        # 현재 정점이 도착 정점 G라면
        # 하나의 경로를 찾았으므로 cnt 증가
        if node_now == G:
            cnt += 1


        # 현재 정점과 연결된 다음 정점들을 하나씩 확인
        for i in matrix[node_now]:

            # 아직 현재 경로에서 방문하지 않은 정점이라면
            if used[i] == 0:

                # 다음 정점 방문 처리
                used[i] = 1

                # 다음 정점으로 이동해서 DFS 계속 진행
                dfs_24220(i)

                # 재귀가 끝나고 돌아오면
                # 다른 경로에서 다시 사용할 수 있도록
                # 방문 기록 원상 복구
                #
                # -> 백트래킹
                used[i] = 0


    # 출발 정점은 이미 방문한 상태로 시작
    used[S] = 1

    # 출발 정점 S에서 DFS 시작
    dfs_24220(S)


    print(f'#{tc} {cnt}')
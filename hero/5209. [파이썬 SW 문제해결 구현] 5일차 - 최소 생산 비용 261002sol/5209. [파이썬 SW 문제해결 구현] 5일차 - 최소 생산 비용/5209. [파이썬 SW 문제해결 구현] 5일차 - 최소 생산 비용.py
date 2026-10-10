import sys
sys.stdin = open("5209. [파이썬 SW 문제해결 구현] 5일차 - 최소 생산 비용/input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # 비용 정보를 저장할 2차원 리스트
    # matrix_vij[i][j]
    # = i번째 제품을 j번째 공장에서 생산할 때 드는 비용
    matrix_vij = []

    for i in range(N):
        row = []
        row.extend(map(int, input().split()))
        matrix_vij.append(row)


    # 지금까지 찾은 최소 비용
    # 처음에는 비교를 위해 무한대로 설정
    answer = float('inf')


    # 각 공장을 이미 사용했는지 체크
    # visited[0] = 1 이면 0번 공장은 이미 사용한 상태
    visited = [0] * N


    def recursion(index_product, current_cost):
        global answer

        # 가지치기
        # 현재까지의 비용이 이미 최소 비용 이상이라면
        # 더 진행해도 최소값이 될 수 없으므로 종료
        if answer <= current_cost:
            return


        # 모든 제품에 공장을 하나씩 배정한 경우
        if index_product >= N:

            # 현재 비용이 기존 최소 비용보다 작으면 갱신
            if current_cost < answer:
                answer = current_cost

            return


        # 현재 제품을 어느 공장에서 생산할지 하나씩 확인
        for index_factory in range(N):

            # 해당 공장을 아직 사용하지 않았다면
            # not 0 == True
            if not visited[index_factory]:

                # 현재 공장을 사용 처리
                visited[index_factory] = 1

                # 다음 제품으로 이동
                # 현재 비용에
                # '현재 제품을 선택한 공장에서 생산하는 비용' 추가
                recursion(
                    index_product + 1,
                    current_cost + matrix_vij[index_product][index_factory]
                )

                # 재귀가 끝나고 돌아왔으므로
                # 다른 경우의 수를 확인하기 위해
                # 사용했던 공장을 다시 미사용 상태로 복구
                # -> 백트래킹
                visited[index_factory] = 0


    # 0번 제품부터 시작
    # 아직 아무 비용도 들지 않았으므로 0
    recursion(0, 0)

    print(f'#{tc} {answer}')
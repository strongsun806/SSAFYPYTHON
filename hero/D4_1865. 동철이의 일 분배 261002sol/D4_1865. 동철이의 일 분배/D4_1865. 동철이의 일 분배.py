import sys
sys.stdin = open("D4_1865. 동철이의 일 분배/input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # 직원별로 각 일을 성공할 확률을 저장하는 2차원 리스트
    # matrix_probability[i][j]
    # = i번 직원이 j번 일을 성공할 확률
    matrix_probability = []

    for i in range(N):
        row = []
        row.extend(map(int, input().split()))
        matrix_probability.append(row)


    # 각 일이 이미 다른 직원에게 배정되었는지 체크
    # visited[j] == 1(True)이면 j번 일은 이미 배정된 상태
    visited = [0] * N

    # 최대 성공 확률을 저장할 변수
    # 최댓값을 구하는 문제이므로 처음에는 0으로 초기화
    max_probability = 0


    def resursion(index_worker, current_probability):
        global max_probability

        # 가지치기
        # 확률은 앞으로 계속 0~1 사이의 값을 곱하게 되므로
        # 현재 확률보다 커질 수 없음
        #
        # 따라서 현재 확률이 이미 구해놓은 최대 확률보다
        # 작거나 같다면 더 내려가볼 필요가 없음
        if current_probability <= max_probability:
            return


        # 모든 직원에게 일을 하나씩 배정한 경우
        if index_worker == N:

            # 지금 완성된 경우의 확률이
            # 기존 최대 확률보다 크다면 갱신
            if current_probability > max_probability:
                max_probability = current_probability

            return


        # 현재 직원에게 어떤 일을 맡길지
        # 모든 일을 하나씩 확인
        for index_job in range(N):

            # 아직 다른 직원에게 배정되지 않은 일이라면
            if not visited[index_job]:

                # 현재 직원이 해당 일을 성공할 확률이 0이면
                # 이후 확률도 무조건 0이 되므로 탐색할 필요 없음
                if matrix_probability[index_worker][index_job] == 0:
                    continue


                # 현재 일을 사용했다고 표시
                visited[index_job] = True


                # 입력값은 0 ~ 100의 퍼센트 값이므로
                # 100으로 나누어서 0 ~ 1 사이의 확률로 변경
                #
                # 지금까지의 확률에
                # 현재 직원이 현재 일을 성공할 확률을 곱해줌
                next_prob = (
                    current_probability
                    * (matrix_probability[index_worker][index_job] / 100)
                )


                # 다음 직원에게 일을 배정하러 재귀 호출
                resursion(index_worker + 1, next_prob)


                # 재귀 탐색이 끝났으므로
                # 현재 일을 다시 미사용 상태로 복구
                #
                # 그래야 현재 직원에게 다른 일을 배정하는
                # 새로운 경우의 수를 탐색할 수 있음
                # -> 백트래킹
                visited[index_job] = False


    # 0번 직원부터 시작
    #
    # 아직 아무 확률도 곱하지 않았으므로
    # 곱셈의 시작값인 1에서 시작
    resursion(0, 1)


    # 내부에서는 확률을 0~1 사이로 계산했으므로
    # 마지막에 다시 * 100 해서 퍼센트로 변환
    # 소수점 아래 6자리까지 출력
    print(f'#{tc} {(max_probability * 100):.6f}')
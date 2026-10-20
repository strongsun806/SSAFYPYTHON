import sys
sys.stdin = open("D3_5208. [SW 문제해결 구현] 5일차 - 전기버스2/input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    # 한 줄에서
    # 첫 번째 값은 정류장 수 N,
    # 나머지는 각 정류장에서 사용할 수 있는 배터리 용량 정보
    N, *list_Mi = map(int, input().split())

    # 문제 입력 특성상
    # 배터리 정보의 개수는 N - 1개
    # 마지막 정류장은 목적지이므로 배터리 정보가 필요 없음
    # N - 1 == len(list_Mi) 일거임 ㅇㅇ

    # print(N)
    # print(list_Mi)


    # 최소 교환 횟수를 저장할 변수
    # 처음에는 아주 큰 값으로 설정
    answer = float('inf')


    # index_now:
    # 현재 위치한 정류장의 "리스트 인덱스"
    # 0번 인덱스 == 실제 1번 정류장
    #
    # count_visit:
    # 지금까지 배터리를 교환한 횟수
    def recursion(index_now, count_visit):
        global answer


        # 가지치기
        # 현재까지의 교환 횟수가
        # 이미 구해놓은 최소 교환 횟수 이상이라면
        # 더 진행해도 더 좋은 답이 나올 수 없음
        if answer <= count_visit:
            return


        # 리스트 인덱스를 실제 정류장 번호로 변환
        # index 0 -> 1번 정류장
        # index 1 -> 2번 정류장
        station_now = index_now + 1


        # 현재 정류장에서 사용할 수 있는 배터리 용량
        battery = list_Mi[index_now]


        # 현재 정류장에서 가진 배터리로
        # 목적지 N번 정류장까지 바로 갈 수 있는 경우
        if station_now + battery >= N:

            # 지금까지의 교환 횟수가
            # 기존 최소값보다 작으면 갱신
            if count_visit < answer:
                answer = count_visit

            # 목적지까지 갈 수 있으므로
            # 더 이상 재귀 진행할 필요 없음
            return


        # 현재 배터리로 갈 수 있는
        # 모든 다음 정류장을 하나씩 시도
        #
        # 예:
        # battery = 3이라면
        # 1칸, 2칸, 3칸 이동 모두 시도
        for move_index in range(1, battery + 1):

            # 다음에 갈 정류장의 리스트 인덱스
            index_next = index_now + move_index

            # 다음 정류장으로 이동해서 재귀 호출
            #
            # 다음 정류장에 도착한 뒤
            # 새 배터리로 갈아끼우게 되므로
            # 교환 횟수 + 1
            recursion(index_next, count_visit + 1)


    # 1번 정류장에서 시작
    # 1번 정류장 == 리스트 인덱스 0
    #
    # 시작할 때 장착되어 있는 배터리는
    # 교환 횟수에 포함하지 않으므로 count_visit = 0
    recursion(0, 0)


    # 최소 배터리 교환 횟수 출력
    print(f'#{tc} {answer}')
    
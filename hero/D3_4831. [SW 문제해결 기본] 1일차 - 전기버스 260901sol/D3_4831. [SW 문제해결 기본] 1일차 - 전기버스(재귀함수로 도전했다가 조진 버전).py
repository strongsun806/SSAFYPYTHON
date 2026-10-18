import sys
sys.stdin = open("D3_4831. [SW 문제해결 기본] 1일차 - 전기버스/input.txt", "r")

T = int(input()) # 노선수 T (1이상 50이하)
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())  # K: 한번 충전으로 최대한 이동할 수 있는 정류장 수
                                         # N: 정류장 개수 인덱스(0번부터 N번 정류장까지 있음)
                                         # M: 충전기 설치가 된 정류장 개수
                                    # 세 수 모두 1이상 100이하
    list_index_adapter = list(map(int, input().split()))  # 충전기 설치가 된 정류장 인덱스 번호 모음

    # 인덱스 0은 출발지점
    # 최대 K칸을 움직일 수 있고, K칸을 움직였을 때 해당칸에 충전소가 없다면 이전의 가장 가까운 충전소에서 충전을 해야한다.
    # 따라서 구현할 때 K칸을 움직이고 해당칸부터 다시 돌아오면서 가장 먼저 충전소가 있다면,
    # 충전 횟수에 카운팅을 +1 하고, 해당 인덱스부터 다시 반복을 하는 방식으로 구현해보고자 한다.

    # 리스트 생성 후, 예시와 같이 정류장의 인덱스와 value값이 같도록 할당
    list_N = []
    for i in range(N+1):
        list_N.append(i)  # [0, 1, 2, ... , N]

    count_charging_station = 0  # 여기에 카운팅하면서 출력값으로 쓸 예정.
    best_idx = 0  # 이 값은 가장 최근에 충전한 충전소의 인덱스값임. 반복문을 돌면서 값이 바뀔거고, 이 위치부터 순회를 다시 시작할 수 있도록 만든거임.
                  # 0으로 시작해서 다른 값으로 할당되면서 사용하는거라서 초기값을 0으로 줌.


    list_for_cal = []  # 밑에 있는 반복을 수행하기 위해 만든 리스트임

    for i in range(0, N + 1):
        list_for_cal.append(0)  # [0, 0, ... , 0] 0이 N개+1

    for i in list_index_adapter:
        list_for_cal[i] = 1  # 충전기의 위치만 1로 재할당



    def find_station(current_position, K, N, list_for_cal):
        # 1. current_position 에서 N까지 한 번에 갈 수 있는 경우 -> 더 이상 충전할 필요가 없음
        if current_position + K >= N:
            return 0

        # 2. current_position 에서 갈 수 있는 가장 오른쪽(current_position + K)부터 역으로 확인
        for next_position in range(current_position + K, current_position, -1):
            if list_for_cal[next_position] == 1:  # 조건을 만족하는 선에서 가장 오른쪽 충전기를 찾았다면,
                                                  # (이 조건은 만족하지 못한다면, 충전기를 못찾은거임)

                # 조건 내에서 가장 오른쪽 충전기를 찾으면 재귀함수 호출
                # next_position 에서 N까지 가는데 필요한 충전 횟수를 구해오기
                result = find_station(next_position, K, N, list_for_cal)  # 여기에서 재귀함수 호출

                # 만약 성공(0 이상의 값)했다면, 이 경로가 정답이므로 내 충전 횟수 +1 해서 바로 리턴하기

                if result != -1:
                    return result + 1
                # 만약 result가 -1이 나왔다면, 리턴값없이 가만히 두기
                # -> 그러면 for문에 의해 그 다음으로 가까운 충전소를 찾아서 또 재귀함수를 호출하는 형식으로 넘어감

        # 3. 범위 내에 충전소가 하나도 없어서 situation impossible인 경우
        return -1


    answer = find_station(0, K, N, list_for_cal)

    # 도달 불가능(-1)인 경우 문제 조건에 따라 0으로 변경
    if answer == -1:
        answer = 0

    print(f"#{test_case} {answer}")


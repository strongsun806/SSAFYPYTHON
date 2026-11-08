import sys
sys.stdin = open("input.txt", "r")

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
    # list_N = []
    # for i in range(N+1):
    #     list_N.append(i)  # [0, 1, 2, ... , N]

    count_charging_station = 0  # 여기에 카운팅하면서 출력값으로 쓸 예정.
    best_idx = 0  # 이 값은 가장 최근에 충전한 충전소의 인덱스값임. 반복문을 돌면서 값이 바뀔거고, 이 위치부터 순회를 다시 시작할 수 있도록 만든거임.
                  # 0으로 시작해서 다른 값으로 할당되면서 사용하는거라서 초기값을 0으로 줌.


    list_for_cal = []  # 밑에 있는 반복을 수행하기 위해 만든 리스트임

    for i in range(0, N + 1):
        list_for_cal.append(0)  # [0, 0, ... , 0] 0이 N개+1

    for i in list_index_adapter:
        list_for_cal[i] = 1  # 충전기의 위치만 1로 재할당


    def find_station(current_position, K, N, list_for_cal):
        # 현재 위치(current_position)에서 한 번의 충전으로 최대 K칸까지 갈 수 있음.
        # 예를 들어 현재 위치가 4이고 K가 5라면 4 -> 9까지 한 번에 갈 수 있음.(3번째 input의 경우. 주의해야할 케이스 중 하나긴 함)

        # 만약 current_position + K가 N 이상이라면 현재 위치에서 목적지 N까지 바로 갈 수 있다는 뜻.
        # 즉, 더 이상 중간 충전소를 들를 필요가 없으므로 추가 충전 횟수는 0번.
        if current_position + K >= N:
            return 0


        # 현재 위치에서 갈 수 있는 가장 먼 위치부터 하나씩 뒤로 오면서 충전소가 있는지 확인함.
        # 예를 들어 current_position = 3, K = 4 라면 갈 수 있는 범위는 4, 5, 6, 7

        # 그중 최대한 멀리 있는 충전소를 먼저 찾고 싶으므로 7 -> 6 -> 5 -> 4 순서로 검사함.
        # range의 끝값 current_position은 포함되지 않음.
        # -> 따라서 현재 위치 자체는 검사하지 않음.
        for next_position in range(current_position + K, current_position, -1):


            # list_for_cal에서
            # 1이면 충전소가 있는 위치
            # 0이면 충전소가 없는 위치.

            # 따라서 현재 검사 중인 next_position에 충전소가 있는지 확인함.
            if list_for_cal[next_position] == 1:


                # 여기까지 들어왔다는 것은 현재 위치에서 갈 수 있는 범위 안에서 가장 멀리 있는 충전소를 찾았다는 뜻임.

                # 이제 그 충전소까지 이동해서 충전했다고 생각하고, 그 위치부터 다시 똑같은 문제를 풀면 됨.

                # 즉, "next_position에서 목적지 N까지 가려면 앞으로 충전을 몇 번 더 해야 하지?" 를 재귀함수에게 물어보는 것임.
                result = find_station(next_position, K, N, list_for_cal)


                # 재귀함수가 -1을 반환했다는 것은 next_position에서 출발해도 목적지 N까지 갈 수 없었다는 뜻임.
                #
                # 이 문제에서는 항상 가장 멀리 있는 충전소를 선택하고 있으므로,
                # 가장 먼 충전소에서조차 목적지까지 갈 수 없다면 그보다 가까운 충전소로 가도 해결되지 않음.
                #
                # -> 더 탐색하지 않고 바로 "도달 불가능"을 의미하는 -1을 반환함.
                if result == -1:
                    return -1


                # 여기까지 왔다는 것은 next_position에서 목적지까지 갈 수 있다는 뜻임.

                # result에는 "next_position부터 목적지까지 필요한 충전 횟수" 가 들어 있음.
                # 그런데 지금 현재 위치에서 next_position 충전소를 한 번 이용했으므로 그 충전 1회를 더해줘야 함.

                # 예를 들어 result = 2 라면, next_position 이후로 충전이 2번 필요하다는 뜻임.
                # 지금 next_position에서 충전하는 것까지 포함하면 총 3번임.
                return result + 1


        # for문을 끝까지 돌았는데도 return이 한 번도 실행되지 않았다는 것은
        # 현재 위치에서 K칸 안에 충전소가 하나도 없었다는 뜻임.

        # -> 더 이상 앞으로 갈 수 없으므로 목적지 도달 불가능.

        # -> -1을 실패 표시로 사용함.
        return -1


    answer = find_station(0, K, N, list_for_cal)

    # 도달 불가능(-1)인 경우 문제 조건에 따라 0으로 변경하기
    if answer == -1:
        answer = 0

    print(f"#{test_case} {answer}")


import sys
sys.stdin = open("[A형대비]_1953 탈주범 검거/sample_input.txt", "r")

from collections import deque

T = int(input()) # 5 총 테스트 개수
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1): # T 이후 input은 처음껀 N M R C L고
                                  # 또 이후 N회만큼 input을 받으며 한 사이클이 끝난다.
    N, M, R, C, L = map(int, input().split())
    matrix = []
    for i in range(N): # 행렬 만들기
        row = []
        for j in map(int, input().split()):
            row.append(j)
        matrix.append(row)

    # for row in matrix: # 만든 행렬 이쁘게 보기
    #     print(row)

    direction_vector = [         (-1, 0),
                        (0, -1),          (0, +1),
                                 (+1, 0),
                        ] # 상[0] 좌[1] 우[2] 하[3]

    # 터널 구조물 type별 vector값 분배하기. list안의 값들은 tuple임
    dv1 = [direction_vector[0], direction_vector[1], direction_vector[2], direction_vector[3]] # type1
    dv2 = [direction_vector[0], direction_vector[3]] # type2
    dv3 = [direction_vector[1], direction_vector[2]] # type3
    dv4 = [direction_vector[0], direction_vector[2]] # type4
    dv5 = [direction_vector[3], direction_vector[2]] # type5
    dv6 = [direction_vector[3], direction_vector[1]] # type6
    dv7 = [direction_vector[0], direction_vector[1]] # type7

    dict_direction = {
        1: dv1, 2: dv2, 3: dv3, 4: dv4, 5: dv5, 6: dv6, 7: dv7
    }


    # matrix[R][C]: 현재 위치
    # for i in range(1, L): # (R, C)에서 시작하는 시점이 이미 1시간 후 이므로 총 L시간이라 생각했을 때
    #                       # L-1 회 움직이면 된다.
    #     if matrix[i][j] == 1:
            
    def path_wherever(R, C, L):
        # 시작 위치(index) 받기 R, C / 처음 시작이든 새롭게 바뀐 시작이든?
        r, c = R, C # (r, c)는 현재위치

        # 초기 deque설정 및 이후에 여기에 담을거임
        deque_for_cal = deque()
        deque_for_cal.append((r, c, 1)) # 초기값 대입. 이후에 밑에 while문에서 순회하며 deque 끝에 추가될거고
                                        # while문이 시작될 때마다 [0]에 해당하는 값이 계속해서 계산될거임(deque가 사라질때까지)

        # 방문했었나를 확인하기 위한 누적 set
        already_visited = set()
        already_visited.add((r, c)) # 일단 처음 들어온 애는 추가
                                  # Loop에서 새로운 값들은 그 안에서 추가 명령하기



        while deque_for_cal: # deque_for_cal가 존재하는 동안 반복문 실행(empty하면 중지되겠지 ㅇㅇ)

            # 그 index의 data를 보고 type을 판단해서 바로 할당.
            # 할당한 값으로 갈 수 있는 곳들을 찾아서 deque에 append하기

            current_r, current_c, current_L = deque_for_cal.popleft()

            if current_L == L: 
                continue

            if matrix[current_r][current_c] in range(1, 8):
                                            # 해당하는 matrix의 data가 1~7의 정수 중에 있다면.
                                            # matrix[r][c]에서
                                            # 매 while마다 r자리에는 deque의 맨 앞 index의 [0]값이 들어가야할거고
                                            # 매 while마다 c자리에는 deque의 맨 앞 index의 [1]값이 들어가야 함.
                                            # pop은 호출마다 실행되므로 한 번 pop을 받아서 값을 담아두고 그 값에서 빼와서 쓰겠음
                for i in range(len(dict_direction[matrix[current_r][current_c]])):
                
                    move_r = dict_direction[matrix[current_r][current_c]][i][0]
                    move_c = dict_direction[matrix[current_r][current_c]][i][1]

                    r, c = current_r + move_r, current_c + move_c

                    if (0 <= r < N) and (0 <= c < M) and (matrix[r][c] > 0) and ((-move_r, -move_c) in dict_direction[matrix[r][c]]):
                        if ((r, c) not in already_visited):
                            already_visited.add((r, c))

                            deque_for_cal.append((r, c, current_L + 1))

                




        # print(count_L)
        # print(deque_for_cal)
        print(f'#{test_case} {len(already_visited)}')

    path_wherever(R, C, L)
import sys
sys.stdin = open("input.txt", "r")

T = int(input())  # 테스트 케이스 받기(1이상 50이하)

for test_case in range(1, T + 1):
    N = int(input())  # (5이상 100이하)

    matrix_maze = []
    for i in range(N):
        a = input()
        row = []
        for j in range(N):
            row.append(int(a[j]))
        matrix_maze.append(row)

    # for i in matrix_maze:
    #     print(i)

    def dfs_maze(matrix_maze_whatever):
        # start 지점에서 end 지점까지 갈 수 있다면 return 1, 안되면 return 0

        # 시작점 위치 찾기
        for i in range(N):
            for j in range(N):
                if matrix_maze_whatever[i][j] == 2:
                    start_row = i
                    start_col = j

        # 후입선출을 위한 stack 만들고, 일단 시작정점을 append하기
        stack_matrix_maze = []
        stack_matrix_maze.append((start_row, start_col))

        # matrix_maze와 같은 모양의 visited를 만들거임
        # 여기에서는 방문에 대한 흔적을 기록하게 될거임 ㅇㅇ
        # 방문을 했다면 1, 아직 안했다면 0으로 기록하겠음 ㅇㅇ
        matrix_visited = []
        for i in range(N):
            row = []
            for j in range(N):
                row.append(0)
            matrix_visited.append(row)

        matrix_visited[start_row][start_col] = 1  # 시작정점은 방문처리하면서 시작해야함 ㅇㅇ


        while stack_matrix_maze:  # stack_matrix_maze가 존재하는 동안 반복
                                  # stack_matrix_maze에서 후입선출의 과정을 반복하면서
                                  # 길이 없으면 pop을 이용해서 없앨건데, 다 없어지면(다 탐색하면)
                                  # 종료가 되도록 설정
            # 현재위치
            # 또는 current에 한번에 받아와도 됨 ㅇㅇ
            current_row, current_col = stack_matrix_maze[-1]

            # 현재위치의 값이 3이라면: 현재위치가 도착위치랑 같다면
            # return 1하기
            if matrix_maze_whatever[current_row][current_col] == 3:
                return 1
            # 이게 while문의 위쪽에 위치한 이유는
            # while 반복문이 끝나고 나서 다시 올라와서 시작하는 시점에 점검을 하며 판단해야하기 때문

            # 현재위치에서 길 찾기(상하좌우)
            for delta_row, delta_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
               # 행 변화량   열 변화량        상       하       좌       우

                # 다음에 봐야할 좌표
                next_row = current_row + delta_row
                next_col = current_col + delta_col

                if (0 <= next_row < N) and (0 <= next_col < N) and (matrix_maze_whatever[next_row][next_col] != 1) and (matrix_visited[next_row][next_col] == 0):
                  #  행이 정상범위인가          열이 정상범위인가              다음에 봐야할 좌표가 1(벽)이 아니라면                          방문도 안했다면

                    # 다음에 봐야할 좌표로서 stack에 append하기
                    stack_matrix_maze.append((next_row, next_col))

                    # matrix_visited에도 방문을 했다고 표시
                    matrix_visited[next_row][next_col] = 1

                    # if문이 움직이는데 있어서 정상적으로 움직이기 위한 조건이었으므로
                    # 움직이고 break로 for문 끊고 다음 반복으로 가기
                    break

            # for-else
            # -> for 루프가 break를 만나 중단되지 않고
            # 끝까지 정상적으로 완료되었을 때만 else 블록이 실행
            # break 문을 만나서 반복문이 종료되면 else의 코드 블록은 실행되지 않음
            else:  # 길이 없다면 돌아가도록 하기
                stack_matrix_maze.pop()

        # while 문이 끝난 직후의 로직인데,
        # 여기까지 온거면 길을 모두 찾아봤지만 못찾은거임(return 1이 안된거임) ㅠㅠ
        return 0

    result = dfs_maze(matrix_maze)
    print(f'#{test_case} {result}')
from collections import deque
import sys
sys.stdin = open("input.txt", "r")

T = int(input()) # 5
for test_case in range(1, 1 + 1):
    N, W, H = map(int, input().split())
    matrix_brick = []
    for i in range(H):
        row = []
        for j in list(map(int, input().split())):
            row.append(j)
        matrix_brick.append(row)
    # 일단 행렬부터 만들고 값 넣기

    # W의 수만큼 순회하면서 가장 많은 벽돌을 깨는 경우를 찾아야함
    # 여기서 포인트는 처음에 많이 깨는 경우도 끝까지 가서는 최댓값이 아닐 수도 있고
    # 처음에 별로 못깨는 경우도 끝까지 가서는 최댓값이 될 수도 있다는거임
    # 결국에 완전 탐색을 해야함
    # DFS와 백트래킹 관련 문제인거같긴함...
    # 근데 안해봄... 할 줄 모름.. ㅠ
    # 그냥 깡으로 해볼건데, fail뜨면 시간복잡도 때문일거임...
    # -> 해봤는데, 안됨... 그냥 공부해서 dfs써보겠음..ㅠ
    # -> 하... 백트래킹도 써야할거 같아서 재귀함수도 다시 봐야함... 혹시나 누군가 이걸 본다면... 재귀함수 빠이팅!
    # 일단 N번의 시도횟수에서 DFS를 써봤음
    # 하... 재귀함수 안에 BFS의 선입선출 queue를 쓰는 함수를 만들어서 집어넣어야하나봄...
    # 만약에 A형 대비를 풀거면 이건 나중에 건드리십쇼 ㅠ

    # 주어진 행렬의 전치행렬 구하기 -> 좌우 연산으로 변경 -> row 각각에서 연산 수행
    # (벽돌깨지기가 완료됐을 때 남은 블럭은 밑으로 밀어줘야하기 때문에 이게 다루기 더 편할거같다고 판단했음)
    matrix_transpose = []
    for i in range(W):
        row = []
        for j in range(H):
            row.append(matrix_brick[j][i])
        matrix_transpose.append(row)


    # N번의 시도횟수에서 DFS써보기
    def count_break(던진횟수):
        if 던진횟수 == N:
            return # 던진횟수가 N이 되면 함수를 끝내고, 호출한 곳으로 돌아가기(재귀함수라서 이런식으로)

        # brick_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # for a in range(len(matrix_transpose)):
        #     for b in range(a):
        #         if matrix_transpose[a][b] == 0:
        #             continue
        #         if matrix_transpose[a][b] in brick_num:
        #             # 부시는 로직 구현
        #             break_num = matrix_transpose[a][b]
        

        for column in range(W): # 해당 블럭의 숫자만큼 주변도 삭제(블럭 추가로 부시기)
            matrix_transpose[a][column] = 0 # 최초의 블럭 일단 삭제(여기서 삭제란, 해당 칸이 0이 되는 것으로 판단했음)
            if (0 <= a+column < H) and (0 <= b < W):
                if matrix_transpose[a+column][b] == 1:
                    matrix_transpose[a+column][b] = 0
            if (0 <= a < H) and (0 <= b+column < W):
                matrix_transpose[a][b+column] = 0
            if (0 <= a-column < H) and (0 <= b < W):
                matrix_transpose[a-column][b] = 0
            if (0 <= a < H) and (0 <= b-column < W):
                matrix_transpose[a][b-column] = 0
            count_break(던진횟수+1)



    # 연쇄반응에 대한 함수(BFS사용)
    def chain_explosion(i, j): # matrix_transpose[i][j]
        i, j = 0, 0 # 초기값 설정
        # 1을 초과하는 값이 나온 블럭을 담아두고 순차적으로 처리해야함(선입선출이므로 queue에 해당할듯)
        list_explosion = deque()

        while list_explosion: # list_explosion의 내용이 존재하는 동안 내내 반복(없어질때까지 반복)
            if matrix_transpose[i][j] > 1:
                list_explosion.append((i, j))
            



# 이 문제에서 내가 AI나 교재 등의 도움을 받은 부분
# -> 
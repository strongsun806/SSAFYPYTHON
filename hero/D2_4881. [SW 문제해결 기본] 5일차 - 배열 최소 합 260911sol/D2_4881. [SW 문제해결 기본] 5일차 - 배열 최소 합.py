import sys
sys.stdin = open("input.txt", "r")

# 우선 이 문제에서 조심해야할 경우의 수:
# 1. 각 행의 최솟값만 늘 모을 수 없는 경우도 있음
#    -> 각 행의 최솟값의 열이 겹치는 경우에는 어느 한 행이 양보를 해야할 수도 있음
# 2. 만약 최솟값이 하나가 아니라면 어떤 index의 최솟값을 써야할지 생각해야함
#    -> 각 행에서 사용하지 않은 열들을 하나씩 선택해보면서 최소합을 찾아야함

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    matrix_min_arr_sum = []
    for i in range(N):
        row = list(map(int, input().split()))
        matrix_min_arr_sum.append(row)

    # matrix는 N x N 이지만, 열에 대해서만 방문 여부를 확인하면 되므로 1차원 list 생성.
    visited_col = [0] * N                                

    def dfs_backtracking_pruning(current_row):
        min_arr_sum = float('inf')  # 문제에서 N개의 행과 각 값이 최대 10이라고 했으므로
                                    # (N * 10)를 써도 됨

        # 종료조건
        # row가 N까지 왔다는것은 0부터 N-1행에서 하나씩 다 고르면서 +1을 했고
        # N에 도착하자마자 return을 하게 했음
        if current_row == N:

            if current_sum < min_arr_sum:
                min_arr_sum = current_sum
            return

        # 현재 row에서 어떤 col을 고를지 전부 확인(완전탐색)
        for col in range(N):

            # 아직 사용하지 않은 열이라면
            if visited_col[col] == 0:

                # 현재 row에서 고른 col값을 1로 재할당해주면서 방문처리
                visited_col[col] = 1

                # 다음 행으로 이동(재귀)
                dfs_backtracking_pruning(current_row + 1)

                # 재귀에서 돌아왔으니 방금 선택했던 열을 다시 원상복구하기(방문 취소)
                visited_col[col] = 0

    dfs_backtracking_pruning(0)
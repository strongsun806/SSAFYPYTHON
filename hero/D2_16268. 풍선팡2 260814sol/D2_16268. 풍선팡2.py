import sys
sys.stdin = open("D2_16268. 풍선팡2/input1.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = []
    for i in range(N):
        row = []
        for j in map(int, input().split()):
            row.append(j)
        matrix.append(row)

    # for row in matrix:
    #     print(row)
    # print(N, M)

    list_sum = []
    
    for i in range(0, N):
        for j in range(0, M):
            list_for_cal = []
            if (0 <= i < N) and (0 <= j < M):
                list_for_cal.append(matrix[i][j])
            if (0 <= i-1 < N) and (0 <= j < M):
                list_for_cal.append(matrix[i-1][j])
            if (0 <= i+1 < N) and (0 <= j < M):
                list_for_cal.append(matrix[i+1][j])
            if (0 <= i < N) and (0 <= j-1 < M):
                list_for_cal.append(matrix[i][j-1])
            if (0 <= i < N) and (0 <= j+1 < M):
                list_for_cal.append(matrix[i][j+1])
            sumsum = sum(list_for_cal)
            # print(list_for_cal)
            list_sum.append(sumsum)

    print(f'#{test_case} {max(list_sum)}')
    
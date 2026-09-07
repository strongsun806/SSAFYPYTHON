import sys
sys.stdin = open("D2_9490. 풍선팡 260815sol/input1.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = []
    for row in range(N):
        row = []
        for i in map(int, input().split()):
            row.append(i)
        matrix.append(row)
  
    list_sum = []
    for i in range(N):
        for j in range(M):
            list_for_cal = []
            if (0 <= i < N) and (0 <= j < M):
                list_for_cal.append(matrix[i][j])
            for k in range(1, matrix[i][j]+1):
                if (0 <= i-k < N) and (0 <= j < M):
                    list_for_cal.append(matrix[i-k][j])
            for k in range(1, matrix[i][j]+1):
                if (0 <= i+k < N) and (0 <= j < M):
                    list_for_cal.append(matrix[i+k][j])
            for k in range(1, matrix[i][j]+1):
                if (0 <= i < N) and (0 <= j-k < M):
                    list_for_cal.append(matrix[i][j-k])
            for k in range(1, matrix[i][j]+1):
                if (0 <= i < N) and (0 <= j+k < M):
                    list_for_cal.append(matrix[i][j+k])
            result_sum = sum(list_for_cal)
            list_sum.append(result_sum)
  
    print(f'#{test_case} {max(list_sum)}')
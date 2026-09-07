import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split()) # 행, 열
arr = [list(map(int, input().split())) for _ in range(N)]


for i in range(M):
    arr_2 = []

    for j in range(N):
        arr_2.append(arr[N-1-j][i])

    print(*arr_2)


for i in range(N):
    arr_2 = []

    for j in range(M):
        arr_2.append(arr[N-1-i][M-1-j])

    print(*arr_2)


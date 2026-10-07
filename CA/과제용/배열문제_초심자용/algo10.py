import sys
sys.stdin = open("algo10_in.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input().split())))

    sero, garo = map(int, input().split())
    my_val = matrix[sero][garo]

    d_sero = [-1, -1, -1, 0, 0, 1, 1, 1]
    d_garo = [-1, 0, 1, -1, 1, -1, 0, 1]

    count = 0
    for i in range(8):
        next_sero = sero + d_sero[i]
        next_garo = garo + d_garo[i]
        if 0 <= next_sero < N and 0 <= next_garo < N:
            if matrix[next_sero][next_garo] > my_val:
                count += 1

    print(f"#{test_case} {count}")

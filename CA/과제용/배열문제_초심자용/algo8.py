import sys
sys.stdin = open("algo8_in.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    listed = list(map(int, input().split()))

    max_num = listed[0]
    max_idx = 0

    for i in range(1, N):
        if listed[i] > max_num:
            max_num = listed[i]
            max_idx = i

    print(f"#{test_case} {max_idx}")

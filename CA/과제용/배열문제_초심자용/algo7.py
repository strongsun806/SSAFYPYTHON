import sys
sys.stdin = open("algo7_in.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    listed = list(map(int, input().split()))

    max_num = listed[0]
    min_num = listed[0]

    for i in range(1, N):
        if listed[i] > max_num:
            max_num = listed[i]
        if listed[i] < min_num:
            min_num = listed[i]

    cha = max_num - min_num
    print(f"#{test_case} {cha}")

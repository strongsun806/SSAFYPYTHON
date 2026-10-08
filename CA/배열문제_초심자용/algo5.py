import sys
sys.stdin = open("algo5_in.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, A, B = map(int, input().split())
    listed = list(map(int, input().split()))

    count = 0
    for i in range(N):
        if A <= listed[i] <= B:
            count += 1

    print(f"#{test_case} {count}")

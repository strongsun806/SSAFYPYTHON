import sys
sys.stdin = open("algo4_in.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    listed = list(map(int, input().split()))

    count = 0
    for i in range(N):
        if listed[i] == K:
            count += 1

    print(f"#{test_case} {count}")

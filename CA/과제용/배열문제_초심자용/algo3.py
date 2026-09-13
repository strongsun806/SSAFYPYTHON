import sys
sys.stdin = open("algo3_in.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    listed = list(map(int, input().split()))

    result = []
    for i in range(N):
        result.append(listed[i] + listed[N - 1 - i])

    print(f"#{test_case}", *result)

import sys
sys.stdin = open("algo1_in.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    listed = list(map(int, input().split()))

    result = []
    for i in range(N - 1, -1, -1):
        result.append(listed[i])

    print(f"#{test_case}", *result)

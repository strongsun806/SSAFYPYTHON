import sys
sys.stdin = open("input.txt", "r")

# T = int(input())
# for test_case in range(1, T + 1):
N, M = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(M):
    i, j = map(int, input().split())
    arr_list = arr[i - 1 : j]
    result = 0

    for a in arr_list:
        result += a

    print(result)
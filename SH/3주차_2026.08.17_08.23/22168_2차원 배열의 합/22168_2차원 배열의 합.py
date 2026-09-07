import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())

sum_arr = 0
for _ in range(N):
    arr = list(map(int, input().split()))
    for num in arr:
        sum_arr += num

print(sum_arr)
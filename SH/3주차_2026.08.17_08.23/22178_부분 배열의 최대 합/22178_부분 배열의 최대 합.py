import sys
sys.stdin = open("input.txt", "r")

N, K = map(int, input().split())
arr = list(map(int, input().split()))

max_sum = 0
for i in range(N - K + 1):
    current_sum = 0
    for j in range(K):
        current_sum += arr[i + j]
    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)

#=====================================================================

N, K = map(int, input().split())
arr = list(map(int, input().split()))

current_sum = sum(arr[:K])
max_sum = current_sum

for i in range(N - K):
    current_sum = current_sum - arr[i] + arr[i + K]

    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)
import sys
sys.stdin = open("input.txt", "r")

N = int(input())
arr = list(map(int, input().split()))

max_arr = arr[0]
min_arr = arr[0]

for num in arr:
    if max_arr < num:
        max_arr = num
    if min_arr > num:
        min_arr = num

print(f"{max_arr} {min_arr}")
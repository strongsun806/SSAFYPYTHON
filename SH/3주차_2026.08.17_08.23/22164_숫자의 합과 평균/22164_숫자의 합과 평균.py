import sys
sys.stdin = open("input.txt", "r")

N = int(input())
arr = map(int, input().split())

sum = 0
arr_len = 0

for num in arr:
    sum = sum + num
    arr_len = arr_len + 1

print(f"{int(sum)} {int(sum / arr_len)}")


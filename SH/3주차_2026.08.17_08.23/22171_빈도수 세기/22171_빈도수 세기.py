import sys
sys.stdin = open("input.txt", "r")

N = int(input())
arr = map(int, input().split())

num_dict = {}
for num in arr:
    num_dict[num] = num_dict.get(num, 0) + 1

for key in sorted(num_dict):
    print(key, num_dict[key])


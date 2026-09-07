import sys
sys.stdin = open("input.txt", "r")

N = int(input())

for test_case in range(1, N + 1):
    alpha = input()
    print(alpha[::-1])
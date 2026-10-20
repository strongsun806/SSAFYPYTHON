import sys
import os
sys.stdin = open(os.path.join(os.path.dirname(__file__), "sample_input.txt"), "r")

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    unicorn = 2 * M - N
    twinhorn = N - M

    print(f"#{test_case} {unicorn} {twinhorn}")
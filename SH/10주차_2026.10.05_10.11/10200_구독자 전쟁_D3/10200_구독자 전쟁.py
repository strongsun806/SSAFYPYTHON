import sys
import os
sys.stdin = open(os.path.join(os.path.dirname(__file__), "sample_input.txt"), "r")

T = int(input())
for test_case in range(1, T+1):
    N, A, B = map(int, input().split())

    max_v = min(A, B)
    min_V = max(0, A + B - N)

    print(f"#{test_case} {max_v} {min_V}")
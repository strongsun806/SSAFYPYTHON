import sys
import os
sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")

T = int(input())
for test_case in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())

    A = P * W

    if W <= R:
        B = Q
    else:
        B = Q + (W - R) * S

    result = min(A, B)

    print(f"#{test_case} {result}")
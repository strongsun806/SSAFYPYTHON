import sys
import os
sys.stdin = open(os.path.join(os.path.dirname(__file__), "sample_input.txt"), "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    S = []
    for _ in range(N):
        S.append(int(input()))

    avg = sum(S) // N

    result = 0
    for i in range(N):
        if S[i] < avg:
            result += (avg - S[i])

    print(f"#{test_case} {result}")
    
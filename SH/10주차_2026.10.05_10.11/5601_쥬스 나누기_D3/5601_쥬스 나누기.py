import sys
import os
sys.stdin = open(os.path.join(os.path.dirname(__file__), "sample_input.txt"), "r")


T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    result = []
    for _ in range(N):
        result.append(f"1/{N}")

    print(f"#{test_case}", *result)
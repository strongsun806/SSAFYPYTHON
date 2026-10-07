import sys
import os
sys.stdin = open(os.path.join(os.path.dirname(__file__), "sample_input.txt"), "r")

# T = int(input())
# for test_case in range(1, T+1):
#     a, b, c = map(int, input().split())

#     max_v = max(a, b, c)
#     min_v = min(a, b, c)
#     sum_v = a + b + c

#     result = (max_v*2 + min_v*2) - sum_v

#     print(f"#{test_case} {result}")


T = int(input())
for test_case in range(1, T+1):
    a, b, c = map(int, input().split())

    if a == b:
        result = c
    elif a == c:
        result = b
    else:
        result = a

    print(f"#{test_case} {result}")

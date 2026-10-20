import sys
import os
sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")

T = int(input())
for test_case in range(1, T+1):
    memory = input().strip()

    current = '0'
    count = 0

    for bit in memory:
        if bit != current:
            count += 1
            current = bit

    print(f"#{test_case} {count}")
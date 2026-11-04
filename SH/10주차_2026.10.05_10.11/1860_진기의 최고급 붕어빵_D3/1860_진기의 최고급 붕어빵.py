import sys
import os
sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")

T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    people = list(map(int, input().split()))
    people.sort()

    result = "Possible"

    for i in range(N):
        time = people[i]

        bread = (time // M) * K

        if bread < i + 1:
            result = "Impossible"
            break

    print(f"#{test_case} {result}")
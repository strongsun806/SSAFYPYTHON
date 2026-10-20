import sys
import os
sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    place = list(map(int, input().split()))

    count = 0
    min_v = 1000000

    for i in range(N):
        distance = abs(place[i])
        if distance < min_v:
            min_v = distance
            count += 1
        elif distance == min_v:
            count += 1

    print(f"#{test_case} {min_v} {count}")
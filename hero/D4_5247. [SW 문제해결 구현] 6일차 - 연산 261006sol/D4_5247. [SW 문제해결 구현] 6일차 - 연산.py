import sys
sys.stdin = open("D4_5247. [SW 문제해결 구현] 6일차 - 연산/input.txt", "r")
from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N, M =map(int, input().split())

    q = deque()
    if N >= M:
        used = [0] * N
    else:
        used = [0] * M

    q.append(N)
    used[N] = 1
    
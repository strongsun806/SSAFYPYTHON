import sys
sys.stdin = open('input.txt')

from collections import deque

T = 10
for tc in range(1, T+1):
    a= input().strip()
    q = deque(map(int, input().split()))

    d = 0
    while True:
        d = d % 5 +1
        x = q.popleft() - d
        if x <= 0:
            q.append(0)
            break
        q.append(x)

    print(f'#{tc}', *q)
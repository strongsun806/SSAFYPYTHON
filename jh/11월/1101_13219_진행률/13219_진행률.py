import sys
sys.stdin = open('sample_input.txt', 'r')

import math

T = int(input())
for tc in range(1, T+1):
    P, X, Y = map(int, input().split())
    dx = X - 50
    dy = Y - 50
    ans = 0
    if dx*dx + dy*dy <= 2500:
        angle = math.degrees(math.atan2(dx,dy))
        if angle < 0:
            angle += 360
        if angle <= P * 3.6:
            ans = 1
    print(f'#{tc} {ans}')
import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    A, B, C, D = map(int, input().split())
    x = max(A, C)
    y = min(B, D)
    ans = y - x
    if ans < 0:
        ans = 0
    print(f'#{tc} {ans}')
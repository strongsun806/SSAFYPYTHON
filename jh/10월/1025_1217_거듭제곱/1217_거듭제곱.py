import sys
sys.stdin = open('input.txt')


T = 10
for _ in range (1, T+1):
    tc = int(input())
    a, b = map(int, input().split())
    ans = 1
    for _ in range(b):
        ans *= a
    print(f'#{tc} {ans}')
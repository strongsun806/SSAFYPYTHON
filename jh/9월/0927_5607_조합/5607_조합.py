import sys
sys.stdin = open('sample_input.txt', 'r')

P = 1234567891
T = int(input())
for tc in range(1, T + 1):
    N, R = map(int, input().split())
    R = min(R, N - R)
    a = 1
    b = 1
    for i in range(1, R + 1):
        a = a * (N - i + 1) % P
        b = b * i % P
    ans = a * pow(b, P - 2, P) % P
    print(f'#{tc} {ans}')
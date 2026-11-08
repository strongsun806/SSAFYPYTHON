import sys
sys.stdin = open('sample_in.txt')

T = int(input())
for tc in range(1, T+1):
    M = int(input())
    ans = 0
    idx = 0
    for i in range(1, M+1):
        ans += i
        idx = i
        if ans >= M:
            break
    print(f'#{tc} {idx}')

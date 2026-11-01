import sys
sys.stdin = open('sin.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = 99999999999
    for i in range(N-K+1):
        ans = min(arr[i + K -1] - arr[i], ans)
    print(f'#{tc} {ans}')
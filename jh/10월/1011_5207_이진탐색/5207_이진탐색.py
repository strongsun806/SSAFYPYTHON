import sys
sys.stdin = open('sample_input.txt', 'r')


def binary_search(s, e, d):
    global cnt
    if s > e:
        return
    mid = (s + e) // 2
    if target == N[mid]:
        cnt += 1
        return
    if target > N[mid]:
        if d == 1:
            return
        s = mid + 1
        binary_search(s, e, 1)
    else:
        if d == -1:
            return
        e = mid - 1
        binary_search(s, e, -1)
               

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    N = list(map(int, input().split()))
    M = list(map(int, input().split()))
    N.sort()
    cnt = 0
    start = 0
    end = len(N) - 1
    for i in M:
        target = i
        binary_search(start, end, 0)
    print(f'#{tc} {cnt}')
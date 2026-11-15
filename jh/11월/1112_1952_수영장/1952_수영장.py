import sys
sys.stdin = open('sample_input.txt','r')


def dfs(m, cost):
    global best
    if cost >= best:
        return
    if m >= 12:
        best = cost
        return
    dfs(m + 1, cost + min(plan[m]*day, month))
    dfs(m + 3, cost + quarter)


T = int(input())
for tc in range(1, T+1):
    day, month, quarter, year = map(int, input().split())
    plan = list(map(int, input().split()))

    best = year
    dfs(0, 0)
    print(f'#{tc} {best}')
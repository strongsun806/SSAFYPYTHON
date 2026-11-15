import sys
sys.stdin = open('re_sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    E = float(input())

    INF = float('inf')
    dist = [INF] * n
    remaining = list(range(1,n))
    cur = 0
    total = 0

    while remaining:
        cx, cy = x[cur], y[cur]
        best_d = INF
        best_i = -1

        for i in range(len(remaining)):
            v = remaining[i]
            dx = x[v] - cx
            dy = y[v] - cy
            d = dx * dx + dy * dy
            if d < dist[v]:
                dist[v] = d
            if dist[v] < best_d:
                best_d = dist[v]
                best_i = i
        total += best_d
        cur = remaining[best_i]

        remaining[best_i] = remaining[-1]
        remaining.pop()

    print(f'#{tc} {int(E*total+0.5)}')

import sys
sys.stdin = open('input.txt')

from collections import deque
T = 10
for tc in range(1, T+1):
    n, s = map(int, input().split())
    data = list(map(int, input().split()))
    a = max(data)
    edge = []
    for i in range(0, n, 2):
        edge.append((data[i], data[i + 1]))
    queue = deque()
    visited = [0]*(a+1)
    ans = 0
    max_cnt = 0
    for start, end in edge:
        if start == s:            
            queue.append((start, end, 1))
    while queue:
        ns, ne, cnt = queue.popleft()
        if visited[ne] == 1:
            continue
        visited[ne] = 1
        if cnt > max_cnt:
            max_cnt = cnt
            ans = ne
        elif cnt == max_cnt:
            ans = max(ans, ne)

        for start, end in edge:
            if start == ne and visited[end] == 0:
                queue.append((start, end, cnt + 1))
    print(f'#{tc} {ans}')
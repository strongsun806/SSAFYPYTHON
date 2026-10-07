import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    min_sum = 100*(N**2)

    def dfs(now, cnt, total):
        global min_sum

        # 이미 최소 비용보다 커졌으면 더 볼 필요 없음
        if total >= min_sum:
            return

        # 모든 구역 방문 완료
        if cnt == N:
            min_sum = min(min_sum, total + arr[now][0])
            return

        # 1 ~ N-1번 구역 중 방문하지 않은 곳 선택
        for next in range(1, N):
            if not visited[next]:
                visited[next] = 1
                dfs(next, cnt + 1, total + arr[now][next])
                visited[next] = 0

    visited[0] = True
    dfs(0, 1, 0)

    print(f"#{tc} {min_sum}")
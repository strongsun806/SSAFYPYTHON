# 5209. 최소 생산 비용
def dfs(row, current_sum):
    global min_cost

    # 가지치기- 누적비용 >= 이미 찾은 최솟값
    if current_sum >= min_cost:
        return # 더 볼 필요 없으니까 return 하기

    # 모든 공장에 제품을 하나씩 다 배정했을 때 최솟값을 갱신
    if row == N:
        min_cost = min(min_cost, current_sum)
        return
    # 현재 공장(행)에 배정할 제품(열) 고르기
    for col in range(N):
        if not visited[col]:
            visited[col] = True
            dfs(row + 1, current_sum + cost_matrix[row][col])
            visited[col] = False  #원래대로 복구하기


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cost_matrix = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N
    # 비용 최댓값: N <= 15, 각 비용 <= 99이므로 15 * 100 = 1500 정도로 하면 충분함
    min_cost = 1500

    dfs(0, 0)

    print(f"#{tc} {min_cost}")
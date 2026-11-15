#5209 - 최소 생산 비용 

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cost_matrix = [list(map(int, input().split())) for _ in range(N)]
    
    # 리스트를 사용하여 내부 함수에서 값을 변경할 수 있도록 함 ([0]에 min_cost 저장)
    min_cost = [float('inf')]
    visited = [False] * N

    def dfs(row, current_cost):
        # 현재까지의 비용이 이미 찾은 최소 비용 이상이면 더 볼 필요 없음 (가지치기 - 다익스트라?)
        if current_cost >= min_cost[0]:
            return
            
        if row == N: # 최소 비용을 찾았을 때
            if current_cost < min_cost[0]: # 만약에 현재 비용이 최소 비용보다 작으면
                min_cost[0] = current_cost #갱신
            return

        for col in range(N): 
            if not visited[col]:
                visited[col] = True
                dfs(row + 1, current_cost + cost_matrix[row][col])
                visited[col] = False

    dfs(0, 0)
    print(f"#{tc} {min_cost[0]}")
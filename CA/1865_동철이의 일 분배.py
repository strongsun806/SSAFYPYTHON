# sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
        
    # 비트마스킹 DP: dp[mask] = 해당 일 배분 상태(mask)에서의 최대 성공 확률
    dp = [0.0] * (1 << N)
    dp[0] = 1.0  # 시작 확률 1.0
    
    for mask in range(1 << N):
        if dp[mask] == 0:
            continue
            
        # 현재 배분할 사람 번호 (선택된 일의 개수)
        person = bin(mask).count('1')
        if person >= N:
            continue
            
        for j in range(N):
            # j번째 일이 아직 배분되지 않았고 성공 확률이 0이 아닌 경우
            if not (mask & (1 << j)) and matrix[person][j] > 0:
                nxt_mask = mask | (1 << j)
                nxt_prob = dp[mask] * (matrix[person][j] / 100.0)
                if nxt_prob > dp[nxt_mask]:
                    dp[nxt_mask] = nxt_prob
                    
    ans = dp[(1 << N) - 1] * 100.0
    print(f"#{tc} {ans:.6f}")

# sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
        
    # DP 테이블 초기화
    dp = [[0] * N for _ in range(N)]
    dp[0][0] = matrix[0][0]
    
    # 맨 윗줄 (오른쪽으로만 이동)
    for j in range(1, N):
        dp[0][j] = dp[0][j - 1] + matrix[0][j]
        
    # 맨 왼쪽 열 (아래쪽으로만 이동)
    for i in range(1, N):
        dp[i][0] = dp[i - 1][0] + matrix[i][0]
        
    # 나머지 칸: 위쪽에서 내려오거나 왼쪽에서 오는 것 중 최솟값 선택
    for i in range(1, N):
        for j in range(1, N):
            dp[i][j] = matrix[i][j] + min(dp[i - 1][j], dp[i][j - 1])
            
    print(f"#{tc} {dp[N - 1][N - 1]}")

# 2001. 파리퇴치 (2차원 배열 완전 탐색/ 슬라이딩 윈도우 기본)
# 핵심 로직 : N * N 격자에서 M *M 크기의 부분합을 가능한 모든 시작점에서 계산해서
# 최댓값을 구하는 것
# 유효 인덱스 범위 : 행과 열의 시작점은 0부터 N-M 까지 이다
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    grid = [list(map(int,input().split())) for _ in range(N)]
    
    max_flies = 0
    
    # M * M 파리채의 좌상단 좌표(r,c) 기준 탐색
    for r in range(N-M + 1):
        for c in range(N-M +1):
            current_sum = 0
            #M * M 영역의 합 계산
            for dr in range(M):
                for dc in range(M):
                    current_sum += grid[r + dr][ c + dc]
            # 최댓값 갱신
            if current_sum > max_flies:
                max_flies = current_sum
    print(f"#{tc} {max_flies}")
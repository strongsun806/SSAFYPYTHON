import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    # 1. N(행의 수), M(열의 수) 입력받기
    N, M = map(int, input().split())
    
    # 2. NxM 격자 형태의 풍선 꽃가루 정보 2차원 리스트로 입력받기
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    # 상, 하, 좌, 우 방향을 나타내는 델타 배열
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    max_flower = 0  # 꽃가루의 최댓값을 저장할 변수
    
    # 3. 모든 좌표 (r, c)를 순회
    for r in range(N):
        for c in range(M):
            # 선택한 풍선의 꽃가루 개수 (이 개수만큼 상하좌우로 추가 발사)
            K = grid[r][c]
            
            # 터뜨린 현재 위치의 꽃가루 개수로 초기화
            current_sum = K
            
            # 4. 상하좌우 4방향으로 뻗어나감
            for d in range(4):
                # 1칸부터 K칸까지 멀어지면서 확인
                for step in range(1, K + 1):
                    nr = r + dr[d] * step
                    nc = c + dc[d] * step
                    
                    # 격자판 범위 안인 경우만 추가
                    if 0 <= nr < N and 0 <= nc < M:
                        current_sum += grid[nr][nc]
            
            # 5. 지금까지 구한 최댓값 갱신
            if current_sum > max_flower:
                max_flower = current_sum
    
    # 6. 정답 출력
    print(f"#{test_case} {max_flower}")
    # ///////////////////////////////////////////////////////////////////////////////////
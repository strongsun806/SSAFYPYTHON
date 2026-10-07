# ========================================================
# 문제: 10966_물놀이를 가자
# 난이도: D4
# 작성자: 윤형섭 (1627575)
# 제출 결과: Pass
# 저장 일시: 2026-10-07 11:26:52
# ========================================================

from collections import deque
# sys.stdin = open("input.txt", "r")
   # 4방향 델타 탐색 (상, 하, 좌, 우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
 T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
         matrix = []
    queue = deque()
    # 방문 및 거리 기록 배열 (-1: 미방문)
    visited = [[-1] * M for _ in range(N)]
         # 판떼기 입력 및 시작점(물 'W') 큐에 삽입
    for i in range(N):
        row = input().strip()
        matrix.append(row)
        for j in range(M):
            if row[j] == 'W':
                visited[i][j] = 0
                queue.append((i, j))
                     total_dist = 0
         # BFS 탐색 (물에서부터 각 땅까지의 최단 거리 계산)
    while queue:
        r, c = queue.popleft()
                 for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
                         # 격자판 범위 안인지 확인
            if 0 <= nr < N and 0 <= nc < M:
                # 미방문인 땅인 경우 거리 갱신 후 큐에 삽입
                if visited[nr][nc] == -1:
                    visited[nr][nc] = visited[r][c] + 1
                    total_dist += visited[nr][nc]
                    queue.append((nr, nc))
                         print(f"#{test_case} {total_dist}")

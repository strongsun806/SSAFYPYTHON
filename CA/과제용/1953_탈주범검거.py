from collections import deque

# 터널 종류별 이동 가능 방향 (0: 상, 1: 하, 2: 좌, 3: 우)
pipe = {
    1: [0, 1, 2, 3],  # 상, 하, 좌, 우
    2: [0, 1],        # 상, 하
    3: [2, 3],        # 좌, 우
    4: [0, 3],        # 상, 우
    5: [1, 3],        # 하, 우
    6: [1, 2],        # 하, 좌
    7: [0, 2]         # 상, 좌
}

# 상, 하, 좌, 우 델타 좌표
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 반대 방향 매핑 (현재 이동 방향의 반대쪽이 다음 파이프에 열려 있어야 연결됨)
opp = {0: 1, 1: 0, 2: 3, 3: 2}

def get_line():
    while True:
        try:
            line = input().strip()
            if line:
                return line
        except EOFError:
            return None

line = get_line()
if line:
    T = int(line)
    for test_case in range(1, T + 1):
        line = get_line()
        if not line:
            break
        N, M, R, C, L = map(int, line.split())
        
        # 터널 지도 생성
        matrix = []
        for _ in range(N):
            matrix.append(list(map(int, get_line().split())))
        
        # 경과 시간 1이면 맨홀 자리 1곳만 가능
        if L == 1:
            print(f"#{test_case} 1")
            continue

        # 방문 체크 및 시간 기록
        visited = [[0] * M for _ in range(N)]
        queue = deque([(R, C)])
        visited[R][C] = 1
        count = 1

        while queue:
            r, c = queue.popleft()

            # 도달 시간이 L이면 더 이상 이동 불가
            if visited[r][c] == L:
                continue

            cur_type = matrix[r][c]
            if cur_type == 0:
                continue

            for direction in pipe[cur_type]:
                nr = r + dr[direction]
                nc = c + dc[direction]

                # 맵 범위 안인지 확인
                if 0 <= nr < N and 0 <= nc < M:
                    # 미방문이고 터널이 있는 칸인 경우
                    if not visited[nr][nc] and matrix[nr][nc] != 0:
                        nxt_type = matrix[nr][nc]
                        # 다음 터널과 연결되어 있는지 확인 후 큐에 삽입
                        if opp[direction] in pipe[nxt_type]:
                            visited[nr][nc] = visited[r][c] + 1
                            count += 1
                            queue.append((nr, nc))

        print(f"#{test_case} {count}")

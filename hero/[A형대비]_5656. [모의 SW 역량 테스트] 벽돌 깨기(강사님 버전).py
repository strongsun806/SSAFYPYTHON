# 가장 많은 벽돌 깨뜨리는 경우의 수 찾기
# 완전탐색: 모든 경우의 수를 다 수행해보고
#          벽돌을 가장 많이 터트리는 경우의 수 찾기

# 000 001 002 003 010 011 등등 다 해봐야함 -> 순열이고 중복순열임
# 구슬을 발사하는 모든 경우의 수를 고려하기
# 연쇄폭발 구현도 해야함
# 연쇄폭발 이후에 벽돌 정리'

# 구슬을 쏘는 모든 경우의 수 수행하는 재귀함수
# 재귀함수 하나에서 하는 역할은 n번째 구슬을 하나의 칸에 쏴보기하는 역할
# bricks: 현재 상태의 벽돌 모양
def shoot(n, bricks):
    # 이미 N개의 구슬을 발사했으면 그만 쏘기(종료 조건)
    if n == N:
        # 구슬 다 쏴봤으니까 이 상태에서 벽돌 상태 확인하기
        return

    # 0번부터 W-1번 칸 중에 한 칸에 구슬 쏘기
    for i in range(W):
        # 구슬 쏘기 전에 원본 벽돌 모양을 복사해서 복사본에 구슬 쏘기
        copy_bricks = [row[:] for row in bricks]
        # i 번에 구슬쏘기
        # n+1 번째 구슬 쏴보기
        shoot(n+1)

# original이 있고 그걸 copy -> copy본을 깰거임
# 그 안에서 target을 깨는건데 그냥 헷갈리지 말라고 파라미터 명을 target_bricks라고 한거임
def bomb(col, target_bricks):
    # 연쇄 시작 지점 찾기
    for i in range(H):
        if target_bricks[i][col]:
            sr = i
            sc = col
            break

    queue = [(sr, sc)]
    check = [[0] * W for _ in range(H)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    while queue:
        cr, cc = queue.pop(0)
        check[cr][cc] = 1  # 터트릴 위치 표시
        length = target_bricks[cr][cc]

        for d in range(4):
            for l in range(length):  # 벽돌 숫자만큼
                nr = cr + dr[d]*l
                nc = cc + dc[d]*l

                # 벽돌이 아직 있고 아직 터트린 벽돌이 아니라면, 터트릴 대상에 추가
                if 0 <= nr < H and 0 <= nc < W\
                and target_bricks[nr][nc] and not check[nr][nc]:  
                    queue.append((nr, nc))

    # 표시가 되어있는 곳 벽돌 없애주기
    for i in range(H):
        for j in range(W):
            if check[i][j]:  # 표시가 되어있으면, 벽돌깨기
                target_bricks[i][j] = 0
    # 남은 벽돌 정리



T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(H)]

    # for row in data:
    #     print(row)

    shoot(0)
import sys
sys.stdin = open('sample_input.txt', 'r')

d = [[0,1],[1,0],[-1,0],[0,-1]]
# 벽돌 부수기
def destroy(r, c, blocks):
    power = blocks[r][c]
    blocks[r][c] = 0
    if power == 0:
        return
    elif power == 1:
        return
    elif power > 1:
        for k in range(1, power):
            for dr, dc in d:
                nr, nc = r+dr*k, c+dc*k
                if 0<=nr<H and 0<=nc<W:
                    destroy(nr, nc, blocks)
    

# 부순 후 밑으로 정렬
def sorting(box):
    for j in range(W):
        for i in range(H-1, 0, -1):
            if box[i][j] == 0:
                a = 1
                while 0 <= i-a < H and box[i-a][j] ==0:
                    a += 1
                if i - a >= 0:
                    box[i][j], box[i-a][j] = box[i-a][j], box[i][j]


# 첫 지점 찾기
def find_area(c, blocks):
    r = 0
    # 컬럼에서의 벽돌 최고 위치 찾기
    for i in range(H):
        if blocks[i][c] != 0:
            r = i
            return r, c
    # 컬럼이 비었을 때
    return -1, -1


# 빈 행렬 확인
def is_empty(blocks):
    for i in range(W):
        if blocks[H-1][i] != 0:
            return False
    return True


# n번 쏘기
def shoot(cnt, blocks):
    global min_v
    # 모든 지점이 0일 때
    if is_empty(blocks):
        min_v = 0       
        return
    if cnt == N:
        local_min = 0
        for i in range(H):
            for j in range(W):
                if blocks[i][j]:
                    local_min += 1
        if local_min < min_v:
            min_v = local_min
        return 
    for i in range(W):
        copy_block = [row[:] for row in blocks]
        # 부수는 위치 찾기
        sr , sc = find_area(i, copy_block)
        # 빈 컬럼일 때 넘기기
        if sr == -1 and sc == -1:
            continue
        destroy(sr, sc, copy_block)
        sorting(copy_block)
        shoot(cnt + 1, copy_block)

T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    blocks = [list(map(int, input().split())) for _ in range(H)]
    min_v = W * H
    cnt = 0
    shoot(0,blocks)
    print(f'#{tc} {min_v}')

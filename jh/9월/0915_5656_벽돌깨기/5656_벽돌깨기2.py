import sys
sys.stdin = open('sample_input.txt', 'r')

d = [[0,1],[1,0],[-1,0],[0,-1]]
# 벽돌 부수기
def destroy(c,blocks):
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
                    destroy(nc)
    sorting(box)

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

# 쏘는 위치 찾기
def shoot(cnt, blocks):
    if cnt == N:
        return
    for i in range(W):
        copy_block = [row[:] for row in blocks]
        destroy(i, copy_block)
        shoot(cnt + 1)

T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    blocks = [list(map(int, input().split())) for _ in range(H)]

    cnt = 0
    shoot(0,blocks)
    print(f'#{tc} {cnt}')

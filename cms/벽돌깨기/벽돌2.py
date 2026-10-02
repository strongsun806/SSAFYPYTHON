import sys
sys.stdin = open("sample_input.txt","r")


result = []
# 공쏘는 곳 정하기
def shoot(cnt,matrix):    # 재귀적으로 모든 경우의수를 다 쏴보기 # 쏘는 행 출력해보기 
    global min_v 
    if cnt == N:
        # print(matrix)
        remain = 0
        for i in range(H):
            for j in range(W):
                if matrix[i][j]:
                    remain += 1
        if remain < min_v:
            min_v = remain
        return 
    
    for i in range(W):
        # i번에 공쏴보기
        copy_matrix = [ row[:] for row in matrix ]
        copy_matrix = bomb(i,copy_matrix) # 벽돌 쏜거..
        shoot(cnt+1, copy_matrix)
        

# matrix 복사를 해서 넣어줄 행렬
def bomb(col,matrix):
    sr = -1
    sc = col
    for i in range(H):
        if matrix[i][col]:
            sr = i
            break


    tmp_matrix = [[0] * W for _ in range(H)]
    # 터뜨릴 벽돌 목록...
    stack = [(sr,sc)]
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    while stack:
        cr,cc = stack.pop()
        tmp_matrix[cr][cc] = 1
        k = matrix[cr][cc] #폭탄 범위
        for d in range(4):
            for l in range(k):
                nr = cr + dr[d]*l
                nc = cc + dc[d]*l
                if 0 <= nr < H and 0<= nc < W and matrix[nr][nc] and not tmp_matrix[nr][nc]:
                    stack.append((nr,nc))
        
    # 없애면 되는데...... 이거 원본 건드리면 안됨!
    for i in range(H):
        for j in range(W):
            if tmp_matrix[i][j]:
                matrix[i][j] = 0

    for i in range(W):
        idx = H -1
        for j in range(H-1,-1,-1):
            if matrix[j][i]:
                matrix[j][i], matrix[idx][i] = matrix[idx][i],matrix[j][i]
                idx -= 1
    return matrix

T = int(input())
for tc in range(1, T+1):
    N,W,H = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(H)]
    min_v = W*H

    shoot(0, matrix)
    print(f'#{tc} {min_v}')
    



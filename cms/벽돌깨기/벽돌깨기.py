import sys
sys.stdin = open("sample_input.txt","r")

T = int(input())
for tc in range(1, T+1):
    N,W,H = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(H)]
    min_v = W*H
    block_num = 0
    for row in matrix:
        for col in row:
            if col :
                block_num +=1

    def dfs(ball, cnt, matrix):
        global min_v
        if ball == N or cnt ==0:
            min_v=min(min_v,cnt)
            return
        
        for j in range(W):
            dest = [row[:] for row in matrix]
            tmp=[]
            n_cnt = cnt
            for i in range(H):
                if dest[i][j]:
                    n_cnt -=1
                    tmp.append([i,j,dest[i][j]])
                    dest[i][j] = 0
                    break
            else :
                continue
            
            while tmp:
                i,j,p = tmp.pop()
                for k in range(1,p):
                    for  di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                        ni, nj = i +di*k, j + dj*k
                        if 0<=ni<H and 0<=nj<W and dest[ni][nj]:
                            if dest[ni][nj]>1:
                                tmp.append([ni,nj,dest[ni][nj]])
                            dest[ni][nj]=0
                            n_cnt -=1
            for i in range(W):
                idx = H -1
                for j in range(H-1,-1,-1):
                    if dest[j][i]:
                        dest[j][i], dest[idx][i] = dest[idx][i],dest[j][i]
                        idx -= 1
            dfs(ball+1, n_cnt,dest)

    dfs(0,block_num,matrix)
    print(f"#{tc} {min_v}")
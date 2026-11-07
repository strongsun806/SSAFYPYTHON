import sys
sys.stdin = open("sample_in.txt","r")

# 연결된 육지 지우기 함수
def dfs(r,c):
    data[r][c]='W'
    dr=[-1,1,0,0]
    dc=[0,0,-1,1]
    for d in range(4):
        nr = r+dr[d]
        nc = c+dc[d]
        if 0<=nr<N and 0<=nc<M and data[nr][nc]=="L":
            dfs(nr,nc)

T= int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    data=[list(input()) for _ in range(N)]

    # data를 행우선순위로 순회 << 중첩 반복
    # 육지를 찾으면 연결된 육지 삭제 < dfs,bfs
    num_of_island = 0
    for i in range(N):
        for j in range(M):
            if data[i][j] == 'L': #육지 찾기
                # 육지면
                num_of_island+=1
                # 이 육지와 연결된 모든 육지를 삭제(섬지우기)
                dfs(i,j)
    print(f"#{tc} {num_of_island}")
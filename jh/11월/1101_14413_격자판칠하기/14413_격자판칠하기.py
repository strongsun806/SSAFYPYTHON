import sys
sys.stdin = open('sample_input.txt', 'r')

def check(r, c):
    global ans
    if data[r][c] == '?':
        return
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < M:
            if data[r][c] == data[nr][nc]:
                ans = 'impossible'
            elif data[nr][nc] == '?':
                if data[r][c] == '#':
                    data[nr][nc] = '.'
                else:
                    data[nr][nc] = '#'
                check(nr, nc)
            

                
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(input().strip()) for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    ans = 'possible'
    for i in range(N):
        for j in range(M):
            check(i, j)
    print(f'#{tc} {ans}')
import sys
sys.stdin = open("sample_input(1).txt", "r")

T = int(input())
for test_case in range(1, T + 1) :
    N, M = map(int, input().split())
    board = []
    black = 0
    white = 0
    # 빈 보드 생성
    for i in range(N):
        board.append(list([0]*N))

    # 초기 흑돌 백돌 배치
    board[N//2-1][N//2-1] = 2
    board[N//2][N//2] = 2
    board[N//2-1][N//2] = 1
    board[N//2][N//2-1] = 1

    # 턴 수 만큼 반복
    for turn in range(M):
        x, y, bw = map(int, input().split())
        board[y-1][x-1] = bw
        for i, j in [(0,1),(0,-1),(-1,0),(1,0),(-1,-1),(-1,1),(1,-1),(1,1)]:
            k=1
            tmp = []
            while 0<=y-1+(i*k)<N and 0<=x-1+(j*k)<N:
                if board[y-1+(i*k)][x-1+(j*k)] == 0 :
                    break
                elif board[y-1+(i*k)][x-1+(j*k)] != bw :
                    tmp.append([(y-1+(i*k)),(x-1+(j*k))])
                elif board[y-1+(i*k)][x-1+(j*k)] == bw:
                    if tmp :
                        for n, m in tmp :
                            board[n][m] = bw
                    break
                k += 1

    # 모든 턴이 끝나고 보드를 완전 참색하면서 흑돌, 백돌 갯수 확인
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1 :
                black += 1
            elif board[i][j] == 2:
                white += 1
    print(f"#{test_case} {black} {white}")
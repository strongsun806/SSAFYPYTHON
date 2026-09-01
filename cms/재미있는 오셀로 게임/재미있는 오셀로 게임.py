import sys
sys.stdin = open("sample_input(1).txt", "r")

T = int(input())
for test_case in range(1, T + 1) :
    N, M = map(int, input().split())
    board = []
    for i in range(N):
        board.append(list([0]*N))
    for turn in range(M):
        x, y, bw = map(int, input().split())
        board[y][x] = bw
        while ()
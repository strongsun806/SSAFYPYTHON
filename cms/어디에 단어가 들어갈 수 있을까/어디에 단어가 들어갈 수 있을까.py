import sys
sys.stdin = open("input.txt", "r")

# 케이스 갯수 할당
T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())

    board = []
    for row in range(N) :
        board.append(list(map(int, input().split())))

    count = 0
    test_row = 0
    test_col = 0
    for row in range(N) :
        for col in range(N) :
            if board[row][col] == 1 :
                test_row += 1
            if board[row][col] == 0 :
                if test_row == K :
                    count += 1
                test_row = 0
        if test_row == K:
            count += 1
        test_row = 0

    for col in range(N) :
        for row in range(N) :
            if board[row][col] == 1 :
                test_col += 1
            if board[row][col] == 0 :
                if test_col == K:
                    count += 1
                test_col = 0
        if test_col == K:
            count += 1
        test_col = 0
    print(f"#{test_case} {count}")            
    
        

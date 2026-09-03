import sys
sys.stdin = open("input.txt","r")

for tc in range(1,11):
    title = int(input())
    board = [list(map(int,input().split())) for _ in range(100)]
    num_max = 0
    dia_sum_1 = 0
    dia_sum_2 = 0
    for i in range(100):
        row_sum = 0
        col_sum = 0
        dia_sum_1 += board[i][i]
        dia_sum_2 += board[i][99-i]

        for j in range(100):
            row_sum += board[i][j]
            col_sum += board[j][i]
        if row_sum > num_max :
            num_max = row_sum
        if col_sum > num_max :
            num_max = col_sum
        if dia_sum_1 > num_max :
            num_max = dia_sum_1
        if dia_sum_2 > num_max :
            num_max = dia_sum_2            

    print(f"#{title} {num_max}")

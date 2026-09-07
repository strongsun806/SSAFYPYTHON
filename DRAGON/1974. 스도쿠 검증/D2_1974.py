total_test_case = int(input())

for current_test_number in range(1, total_test_case + 1):
    
    line_0 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    line_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    line_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    line_3 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    line_4 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    line_5 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    line_6 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    line_7 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    line_8 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    sudoku_board = [line_0, line_1, line_2, line_3, line_4, line_5, line_6, line_7, line_8] #스도쿠판 잘만들었죠?

    input_line_0 = input().split()
    for Vertical_line in range(9):
        sudoku_board[0][Vertical_line] = int(input_line_0[Vertical_line])
        
    input_line_1 = input().split()
    for Vertical_line in range(9):
        sudoku_board[1][Vertical_line] = int(input_line_1[Vertical_line])
        
    input_line_2 = input().split()
    for Vertical_line in range(9):
        sudoku_board[2][Vertical_line] = int(input_line_2[Vertical_line])
        
    input_line_3 = input().split()
    for Vertical_line in range(9):
        sudoku_board[3][Vertical_line] = int(input_line_3[Vertical_line])
        
    input_line_4 = input().split()
    for Vertical_line in range(9):
        sudoku_board[4][Vertical_line] = int(input_line_4[Vertical_line])
        
    input_line_5 = input().split()
    for Vertical_line in range(9):
        sudoku_board[5][Vertical_line] = int(input_line_5[Vertical_line])
        
    input_line_6 = input().split()
    for Vertical_line in range(9):
        sudoku_board[6][Vertical_line] = int(input_line_6[Vertical_line])
        
    input_line_7 = input().split()
    for Vertical_line in range(9):
        sudoku_board[7][Vertical_line] = int(input_line_7[Vertical_line])
        
    input_line_8 = input().split()
    for Vertical_line in range(9):
        sudoku_board[8][Vertical_line] = int(input_line_8[Vertical_line])

    is_sudoku_correct = 1

    for Horizontal_line in range(9): #가로줄
        count_box = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #빈 상자 준비
        for Vertical_line in range(9): # 가로줄 안에서 왼쪽부터 오른쪽으로 9칸 확인
            target_number = sudoku_board[Horizontal_line][Vertical_line] # 현재 칸에 적힌 숫자를 가져옴
            count_box[target_number] = count_box[target_number] + 1 # 해당 숫자의 칸에 1을 더해줌
            
        for num_check in range(1, 10): # 1부터 9까지 반복
            if count_box[num_check] != 1: # 만약 숫자가 1번 나오지 않았다면
                is_sudoku_correct = 0

    for Vertical_line in range(9): #세로줄
        count_box = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #빈 상자
        for Horizontal_line in range(9): # 세로줄 안에서 위에서 아래로 9칸 확인
            target_number = sudoku_board[Horizontal_line][Vertical_line] # 현재 칸에 적힌 숫자를 가져옴
            count_box[target_number] = count_box[target_number] + 1 # 해당 숫자의 칸에 1을 더해줌
            
        for num_check in range(1, 10): # 1부터 9까지 반복
            if count_box[num_check] != 1: # 만약 숫자가 1번 나오지 않았다면
                is_sudoku_correct = 0


    for box in range(0, 9, 3): # 3x3 격자의 시작 가로줄 위치 (0, 3, 6)
        for start_Vertical in range(0, 9, 3): # 3x3 격자의 시작 세로줄 위치 (0, 3, 6)
            count_box = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #빈 상자 준비
            for Horizontal_line in range(3): # 시작 위치부터 아래로 3칸 반복
                for Vertical_line in range(3): # 시작 위치부터 오른쪽으로 3칸 반복
                    target_number = sudoku_board[box + Horizontal_line][start_Vertical + Vertical_line] # 3x3 안의 숫자를 가져옴
                    count_box[target_number] = count_box[target_number] + 1 # 숫자의 개수 1 증가
            
            for num_check in range(1, 10): # 1부터 9까지 반복
                if count_box[num_check] != 1: # 만약 1번 나오지 않았다면
                    is_sudoku_correct = 0

    print("#" + str(current_test_number) + " " + str(is_sudoku_correct))

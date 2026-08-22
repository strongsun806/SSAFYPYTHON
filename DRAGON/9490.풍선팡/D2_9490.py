
#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for t in range(1, T + 1):
    
    line = input()
    temp = ""
    max_x = 0
    max_y = 0

    for char in line:
        if char == " ":
            max_x = int(temp)
            temp = ""
        else:
            temp = temp + char
    max_y = int(temp)


    board = [] # 가장자리 때문에 바깥을 0으로 감싸기
    for _ in range(max_x + 2):
        row = []
        for _ in range(max_y + 2):
            row = row + [0]
        board = board + [row]


    for x in range(1, max_x + 1): # x번째 행의 y번째 열에 데이터 넣는 바구니 생성
        line = input()
        temp = ""
        y = 1

        for char in line:
            if char == " ":
                board[x][y] = int(temp)
                y = y + 1
                temp = ""
            else:
                temp = temp + char
        board[x][y] = int(temp)

    # 중앙 + 상 + 하 + 좌 + 우 돌리기
    max_result = 0 

    for x in range(1, max_x + 1):
        for y in range(1, max_y + 1):
            

            current_sum = ( 
                board[x][y] + board[x - 1][y] + board[x + 1][y] + board[x][y - 1] + board[x][y + 1] # 중앙 + 상 + 하 + 좌 + 우
            )

            if current_sum > max_result: # 최댓값
                max_result = current_sum

    print(f"#{t} {max_result}")
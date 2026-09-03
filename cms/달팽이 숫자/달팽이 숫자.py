import sys
sys.stdin = open("input.txt","r")

# 테스트 케이스 갯수 T
T = int(input())
for tc in range (1,T+1):
    # 가로세로 칸 갯수 length
    length = int(input())
    # length 길이만큼 요소 0을 가진 2차원 배열 board 생성
    board = [[0]*length for _ in range(length)]

    # 행 이동 백터 row_v, 열 이동 백터 col_v 모두 1로 초기화
    row_v = 1
    col_v = 1
    # 행,열 이동을 판별한 switch 변수, False로 초기화
    switch = False
    # 시작 좌표 x, y를 0,0으로 초기화
    x,y = 0,0

    # 1 ~ length**2 까지의 숫자를 board에 추가하는 반복문
    for i in range(1,length**2+1):
        # x,y좌표에 맞춰 순서대로 숫자 할당
        board[y][x]= i

        # switch가 False일 경우, 행 변경
        if switch == False:

            # x를 row_v값 만큼 이동했을 때, 인덱스 오류가 나지 않고, 아직 숫자를 할당 받지 않은 자리면
            if 0<=x+row_v<length and board[y][x+row_v] == 0:
                # x값을 row_v만큼 이동
                x += row_v

            # 인덱스 오류가 나거나, 이동한 곳에 이미 숫자가 할당되어 있으면
            else :
                # 다음 행 이동 백터 값을 반대로 조정
                row_v *= (-1)
                # 다음 부터는 열 이동
                switch = True
                # y값을 col_v만큼 이동
                y += col_v

        # switch가 True 일 경우, 열 변경 
        else :
            # y를 col_v값 만큼 이동했을 때, 인덱스 오류가 나지 않고, 아직 숫자를 할당 받지 않은 자리면
            if 0<=y+col_v<length and board[y+col_v][x]==0:
                # y값을 col_v만큼 이동
                y += col_v

            # 인덱스 오류가 나거나, 이동한 곳에 이미 숫자가 할당되어 있으면          
            else : 
                # 다음 열 이동 백터 값을 반대로 조정   
                col_v *= (-1)
                # 다음 부터는 행 이동
                switch = False
                # x값을 row_v만큼 이동
                x += row_v

    print(f"#{tc}")
    for i in range(length):
        for j in range(length):
            # 열 마다 공백으로 출력
            print(f"{board[i][j]}", end=" ")
        # 행 마다 개행
        print()


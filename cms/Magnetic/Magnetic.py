import sys
sys.stdin = open("input.txt", "r")

#케이스 10개 순환
for test_case in range(1,11):
    # 한변의 길이를 length에 할당
    length = int(input())

    # 100x100 테이블을 board에 2차원 배열로 할당
    board = []
    for i in range(length):
        board.append(list(map(int,input().split())))

    # 긱 테스트 케이스의 교착 상태 개수를 result에 초기화
    result = 0

    # 중복 반복문으로 1열부터 100열 까지 한 행 씩 값 확인
    for col in range(length):
        # 해당 열에 교착상태를 파악하기 위한 state 를 Boolian 으로 할당
        state = None
        for row in range(length):
            # 1행부터 확인하면서, 빨간 자성체가 있으면 state를 False로 변경
            if board[row][col] == 1 :
                state = False

            # 파란 자성체가 나왔을 때, 위 행에 빨간 자성체가 있어서 state가 False이면 교착 상태가 발생
            if board[row][col] == 2 and state == False:
                # state를 True로 바꾸고, 교착 상태 개수 result값을 +1
                state = True
                result += 1

            # 만약 빨간 자성체 다음에 파란 자성체를 못 만나면 state는 False 상태에서 종료(교착 상태 개수 증가 안함)
            # 만약 파란 자성체 이전에 빨간 자성체가 없어서 state가 False가 아니라면 교착 상태 없이 종료
    print(f"#{test_case} {result}")            


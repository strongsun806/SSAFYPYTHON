import sys
sys.stdin = open("sample_input.txt", "r")

# 테스트 케이스 갯수 = T
T = int(input())
# T 만큼 반복
for tc in range(1, T+1):
    # 요소가 0인 10x10 2차원 배열 board
    board = [[0]*10 for _ in range(10)]
    # 칠할 영역 갯수 = color_sq
    color_sq = int(input())
    # 보라색 칸 수 = purple_cnt를 0으로 초기화
    purple_cnt = 0
    # color_sq 만큼 반복
    for sq in range(color_sq):
        # 사각형 정보 가져오기
        x1, y1, x2, y2, color = map(int, input().split())
        # 가로 길이 x2-x1 만큼 i값을 0에서 1씩 늘리며 반복
        for i in range(x2-x1+1):
            # 세로 길이 y2-y1 만큼 j값을 0에서 1씩 늘리며 반복
            for j in range(y2-y1+1):
                # board에서 해당 인덱스의 값이 0이면 color 값으로 재할당
                if board[y1+j][x1+i] == 0 :
                    board[y1+j][x1+i] = color
                #  board에서 해당 인덱스의 값이 0이 아니고 (이미 색칠되어 있고),
                #  색칠된 색이 색칠할 색(color)과 같지 않고, 보라색이 아니면(값이 3이 아니면)
                elif board[y1+j][x1+i] !=color and board[y1+j][x1+i] !=3 :
                    # 그 인덱스 값을 3으로 재할당(보라색으로 색칠)
                    board[y1+j][x1+i] = 3
                    # 보라색으로 칠한 횟수(purple_cnt) +1
                    purple_cnt += 1

    print(f"#{tc} {purple_cnt}")
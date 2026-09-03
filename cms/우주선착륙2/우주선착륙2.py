import sys
sys.stdin = open("input2.txt","r")

# 테스트 케이스 = T
T = int(input())
for tc in range(1,T+1):
    # 행 갯수 N, 열 갯수 M
    N, M = map(int,input().split())

    # 행 갯수 N 만큼 input값을 리스트 요소로 한 board 생성
    board = [list(map(int,input().split()))for _ in range(N)]

    # 탐색해야할 상대적 좌표 리스트 find_scale
    find_scale = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]

    # 4곳 이상 촬영 가능한 자리 갯수 cnt, 0으로 초기화
    cnt = 0

    # 이중 반복문 : board의 모든 자리르 기준으로 주변 좌표 값 탐색
    for i in range(N):
        for j in range(M):
            # 촬영 가능한 곳 개수 can_find, 0으로 초기화
            can_find = 0
            # 상대적 x좌표 k, 상대적 y좌표 l 을 find_scale에서 가져와서 반복 
            for k, l in find_scale :
                # i+l과 j+k의 인덱스가 존재하면 실행
                if 0<=i+l<N and 0<=j+k<M:
                    # 주변 좌표의 값이 기준 좌표 값보다 작으면 can_find + 1
                    if board[i+l][j+k]<board[i][j]:
                        can_find += 1
            # 기준 좌표의 촬영 가능 갯수가 4곳 이상이면 cnt + 1
            if can_find >= 4 :
                cnt += 1

    print(f"#{tc} {cnt}")

        

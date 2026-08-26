import sys
sys.stdin = open("input1.txt", "r")

# 케이스 갯수 할당
T = int(input())
for test_case in range(1, T + 1):
    # 행과 열 개수 할당
    row, col = map(int, input().split())
    # 2차원 배열 리스트 board 초기화 and 할당
    board = []
    for i in range(row):
        board.append(list(map(int,input().split())))
    # 최댓값 result 초기화
    result = 0

    # 모든 요소를 순환하는 중복 반복문
    for i in range(row):
        for j in range(col):
            # 총 꽃가루 개수 count 초기화
            count = 0
            # 해당 풍선의 꽃가루 개수를 num에 할당
            num = board[i][j]
            # 해당 풍선의 꽃가루 개수를 count에 합산
            count += num
            # 해당 풍선의 상하 좌우 풍선의 꽃가루 개수 확인(IndexError회피)
            # 위쪽 인덱스 확인
            if i-1 >= 0 :
                count += board[i-1][j]
            # 아래쪽 인덱스 확인
            if i+1 <= len(board)-1:
                count += board[i+1][j]
            # 왼쪽 인덱스 확인
            if j-1 >= 0 :
                count += board[i][j-1]
            # 오른쪽 인덱스 확인
            if j+1 <= len(board[i])-1:
                count += board[i][j+1]
            # count가 test_case에서 최대이면 result에 할당
            if count > result :
                result = count
    print(f"#{test_case} {result}")
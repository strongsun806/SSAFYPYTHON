import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    # 풍선 배열 만들기
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 출력할 꽃가루의 최대값 초기값 설정
    max_flower = 0
    # 상하좌우 방향 설정을 위한 인덱스 덧셈, 뺄셈 정의
    dr = [-1, 1, 0, 0] # 상, 하
    dc = [0, 0, -1, 1] # 좌, 우
    # 풍선 배열에서 모든 칸을 하나씩 출력
    for i in range(N):
        for j in range(M):
            # 해당 위치의 꽃가루 개수를 할당
            flower = arr[i][j]
            # 상하좌우의 인덱스 값 계산하기
            for k in range(4):
                    nr = i + dr[k] # 상, 하의 인덱스 계산
                    nc = j + dc[k] # 좌, 우의 인덱스 계산
                    # 상하좌우의 인덱스가 배열 안에 있는지 확인하기
                    if 0 <= nr < N and 0 <= nc < M:
                        # 배열 안에 있다면 추가로 더하기
                        flower += arr[nr][nc]
                    else:
                        # 배열 안에 없다면 0을 더하기
                        flower += 0
            # 최대값 변경 시 재할당
            if max_flower < flower:
                max_flower = flower

    print(f"#{test_case} {max_flower}")



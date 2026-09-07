import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0

    # 가로 검사
    for i in range(N):
        count = 0

        for j in range(N):
            if arr[i][j] == 1:
                count += 1
            else:
                if count == K:
                    result += 1
                count = 0

        # 행의 끝까지 왔을 때 확인
        if count == K:
            result += 1

    # 세로 검사
    for j in range(N):
        count = 0

        for i in range(N):
            if arr[i][j] == 1:
                count += 1
            else:
                if count == K:
                    result += 1
                count = 0

        # 열의 끝까지 왔을 때 확인
        if count == K:
            result += 1

    print(f"#{test_case} {result}")
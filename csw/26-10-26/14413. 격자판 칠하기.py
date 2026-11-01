T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    grid = [input().strip() for _ in range(N)]

    ok = [True, True]
    for i in range(N):
        for j in range(M):
            c = grid[i][j]
            if c == '?':
                continue
            for p in range(2):  # p = 0일 때, p = 1일 때 각각 검사
                if (i + j) % 2 == p:    # 이 칸이 패턴 p에서 '#'
                    expected = '#'
                else:   # 아니면 '.'
                    expected = '.'
                if c != expected:   # 실제 칸이 원하는 색과 다르면
                    ok[p] = False   # 불가능
    if ok[0] or ok[1]:
        print(f'#{tc} possible')
    else:
        print(f'#{tc} impossible')
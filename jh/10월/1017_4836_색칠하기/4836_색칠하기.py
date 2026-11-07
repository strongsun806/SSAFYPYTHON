import sys
sys.stdin = open('sample_input.txt','r')
T = int(input())
for tc in range(1, T+1):
    N = int(input().strip())
    # 10*10격자
    arr = [[0]*10 for _ in range(10)]
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2+1):
            for c in range(c1, c2 + 1):
                if arr[r][c] == 0:
                    arr[r][c] = color
                if arr[r][c] == 1 and color == 2:
                    arr[r][c] += color
                if arr[r][c] == 2 and color == 1:
                    arr[r][c] += color
    cnt = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                cnt += 1
    print(f'#{tc} {cnt}')

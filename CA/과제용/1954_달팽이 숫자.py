# Problem: 1954_달팽이 숫자
# Author: 윤형섭_1627575 (Pass)
# Saved by Aura for Boss 💋

T = int(input())
 for tc in range(1, T + 1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
         di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
         i = 0
    j = 0
    d = 0
         for k in range(1, n * n + 1):
        arr[i][j] = k
                 ni = i + di[d]
        nj = j + dj[d]
                 if ni < 0 or ni >= n or nj < 0 or nj >= n or arr[ni][nj] != 0:
            d = (d + 1) % 4
            ni = i + di[d]
            nj = j + dj[d]
                     i = ni
        j = nj
             print(f"#{tc}")
    for i in range(n):
        print(*arr[i])

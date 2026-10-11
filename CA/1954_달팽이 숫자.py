# ========================================================
# 문제: 1954_달팽이 숫자
# 난이도: D2
# 작성자: 윤형섭 (1627575)
# 제출 결과: Pass
# 저장 일시: 2026-10-07 11:41:32
# ========================================================

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

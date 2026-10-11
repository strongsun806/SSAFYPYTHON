# ========================================================
# 문제: 1210_[S/W 문제해결 기본] 2일차 - Ladder1
# 난이도: D4
# 작성자: 윤형섭 (1627575)
# 제출 결과: Pass
# 저장 일시: 2026-10-07 11:41:52
# ========================================================

for _ in range(1, 11):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    i = 99
    j = 0
    for k in range(100):
        if ladder[99][k] == 2:
            j = k
            break
         for i in range(99, 0, -1):
        if j > 0 and ladder[i][j - 1] == 1:
            for k in range(j, -1, -1):
                if k == 0 or ladder[i][k - 1] == 0:
                    j = k
                    break
        elif j < 99 and ladder[i][j + 1] == 1:
            for k in range(j, 100):
                if k == 99 or ladder[i][k + 1] == 0:
                    j = k
                    break
    print(f"#{tc} {j}")

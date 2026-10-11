# ========================================================
# 문제: 2005_파스칼의 삼각형
# 난이도: D2
# 작성자: 윤형섭 (1627575)
# 제출 결과: Pass
# 저장 일시: 2026-10-07 11:37:35
# ========================================================

def factorial(k):
    if k <= 1:
        return 1
    return k * factorial(k - 1)
 def comb(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))
 t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    print(f'#{tc}')
    for n in range(N):
        row = [comb(n, r) for r in range(n + 1)]
        print(*row)

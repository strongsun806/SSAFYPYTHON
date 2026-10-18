# ========================================================
# 문제: 12510_2일차 - 특별한 정렬
# 난이도: D3
# 작성자: 윤형섭 (1627575)
# 제출 결과: Pass
# 저장 일시: 2026-10-07 11:41:01
# ========================================================

T = int(input())
 for tc in range(1, T + 1):
    N = int(input())
    a = sorted(list(map(int, input().split())))
         res = []
    l, r = 0, N - 1
         for i in range(10):
        if i % 2 == 0:
            res.append(a[r])
            r -= 1
        else:
            res.append(a[l])
            l += 1
                 print(f"#{tc}", *res)

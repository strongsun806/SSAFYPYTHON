# ========================================================
# 문제: 20551_증가하는 사탕 수열
# 난이도: D3
# 작성자: 윤형섭 (1627575)
# 제출 결과: Pass
# 저장 일시: 2026-10-07 11:33:39
# ========================================================

T = int(input())
for test_case in range(1, T + 1):
    A, B, C = map(int, input().split())
    eat_count = 0
     if B >= C:
        diff = B - (C - 1)
        eat_count += diff
        B = C - 1
     if A >= B:
        diff = A - (B - 1)
        eat_count += diff
        A = B - 1
     if A <= 0 or B <= 0 or C <= 0:
        print(f"#{test_case} -1")
    else:
        print(f"#{test_case} {eat_count}")

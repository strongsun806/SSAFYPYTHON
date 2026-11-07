# ========================================================
# 문제: 13067_5202. [파이썬 S/W 문제해결 구현] 3일차 - 화물 도크
# 난이도: D3
# 작성자: 윤형섭 (1627575)
# 제출 결과: Pass
# 저장 일시: 2026-10-07 11:28:04
# ========================================================

T = int(input())
 for t in range(1, T + 1):
    N = int(input())
    tasks = []
         for _ in range(N):
        s, e = map(int, input().split())
        tasks.append((s, e))
             tasks.sort(key=lambda x: (x[1], x[0]))
         count = 0
    current_end = 0
         for s, e in tasks:
        if s >= current_end:
            count += 1
            current_end = e
                 print(f"#{t} {count}")

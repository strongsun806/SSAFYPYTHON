# ========================================================
# 문제: 12940_5177. [파이썬 S/W 문제해결 기본] 8일차 - 이진 힙
# 난이도: D2
# 작성자: 윤형섭 (1627575)
# 제출 결과: Pass
# 저장 일시: 2026-10-07 11:30:29
# ========================================================

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
     heap = [0] * (N + 1)
    last = 0
     for i in range(len(numbers)):
        last += 1
        heap[last] = numbers[i]
         c = last
        p = c // 2
        while p > 0 and heap[p] > heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            c = p
            p = c // 2
     ans = 0
    cur = N // 2
    while cur > 0:
        ans += heap[cur]
        cur = cur // 2
     print(f"#{tc} {ans}")

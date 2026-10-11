# ========================================================
# 문제: 10580_전봇대
# 난이도: D3
# 작성자: 윤형섭 (1627575)
# 제출 결과: Pass
# 저장 일시: 2026-10-07 11:33:24
# ========================================================

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lines = []
    for _ in range(N):
        A, B = map(int, input().split())
        lines.append((A, B))
             count = 0
      for i in range(N):
        for j in range(i + 1, N):
            if (lines[i][0] - lines[j][0]) * (lines[i][1] - lines[j][1]) < 0:
                count += 1
                     print(f"#{test_case} {count}")

# ========================================================
# 문제: 12941_5178. [파이썬 S/W 문제해결 기본] 8일차 - 노드의 합
# 난이도: D3
# 작성자: 윤형섭 (1627575)
# 제출 결과: Pass
# 저장 일시: 2026-10-07 11:30:44
# ========================================================

# import sys
# sys.stdin = open("input.txt", "r")
 T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 2)
     for i in range(M):
        node, val = map(int, input().split())
        tree[node] = val
     for i in range(N, 1, -1):
        tree[i // 2] += tree[i]
     print(f"#{tc} {tree[L]}")

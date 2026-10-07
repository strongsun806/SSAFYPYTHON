# ========================================================
# 문제: 12939_5176. [파이썬 S/W 문제해결 기본] 8일차 - 이진탐색
# 난이도: D2
# 작성자: 윤형섭 (1627575)
# 제출 결과: Pass
# 저장 일시: 2026-10-07 11:30:14
# ========================================================

# import sys
# sys.stdin = open("input.txt", "r")
 def inorder(node):
    global count
    if node <= N:
        inorder(node * 2)
        tree[node] = count
        count += 1
        inorder(node * 2 + 1)
 T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)
    count = 1
     inorder(1)
     print(f"#{tc} {tree[1]} {tree[N // 2]}")

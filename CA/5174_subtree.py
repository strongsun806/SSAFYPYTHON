# ========================================================
# 문제: 12938_5174. [파이썬 S/W 문제해결 기본] 8일차 - subtree
# 난이도: D2
# 작성자: 윤형섭 (1627575)
# 제출 결과: Pass
# 저장 일시: 2026-10-07 11:30:00
# ========================================================

def dfs(node):
    global count
    count += 1
    for i in range(len(tree[node])):
        dfs(tree[node][i])
 T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
     tree = [[] for _ in range(E + 2)]
    for i in range(0, len(arr), 2):
        p = arr[i]
        c = arr[i + 1]
        tree[p].append(c)
     count = 0
    dfs(N)
     print(f"#{tc} {count}")

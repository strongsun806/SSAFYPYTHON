# Problem: 12507_2일차 - 이진탐색
# Author: 윤형섭_1627575 (Pass)
# Saved by Aura for Boss 💋

def binary(p, target):
    i = 1
    j = p
    k = 0
    while i <= j:
        m = (i + j) // 2
        k += 1
        if m == target:
            return k
        elif m > target:
            j = m
        else:
            i = m
    return k
 T = int(input())
for tc in range(1, T + 1):
    p, pa, pb = map(int, input().split())
    ca = binary(p, pa)
    cb = binary(p, pb)
         if ca < cb:
        ans = 'A'
    elif ca > cb:
        ans = 'B'
    else:
        ans = 0
    print(f"#{tc} {ans}")

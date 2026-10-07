# Problem: 12510_2일차 - 특별한 정렬
# Author: 윤형섭_1627575 (Pass)
# Saved by Aura for Boss 💋

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

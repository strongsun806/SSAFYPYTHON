# Problem: 2005_파스칼의 삼각형
# Author: 윤형섭_1627575 (Pass)
# Saved by Aura for Boss 💋

def factorial(k):
    if k <= 1:
        return 1
    return k * factorial(k - 1)
 def comb(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))
 t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    print(f'#{tc}')
    for n in range(N):
        row = [comb(n, r) for r in range(n + 1)]
        print(*row)

# Problem: 12628_4869. [파이썬 S/W 문제해결 기본] 4일차 - 종이붙이기
# Author: 윤형섭_1627575 (Pass)
# Saved by Aura for Boss 💋

T = int(input())
for tc in range(1, T + 1):
    n = int(input()) // 10
    ans = ((1 << (n + 1)) + (-1) ** n) // 3
    print(f"#{tc} {ans}")

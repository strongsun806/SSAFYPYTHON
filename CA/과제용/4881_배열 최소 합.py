# Problem: 12675_4881. [파이썬 S/W 문제해결 기본] 5일차 - 배열 최소 합
# Author: 윤형섭_1627575 (Pass)
# Saved by Aura for Boss 💋

def solve():
    T = int(input())
    for tc in range(1, T + 1):
        N = int(input())
        matrix = [list(map(int, input().split())) for _ in range(N)]
        min_sum = 100 * N
                 def dfs(row, current_sum, visited):
            nonlocal min_sum
            if current_sum >= min_sum:
                return
            if row == N:
                if current_sum < min_sum:
                    min_sum = current_sum
                return
                         for col in range(N):
                if not visited[col]:
                    visited[col] = True
                    dfs(row + 1, current_sum + matrix[row][col], visited)
                    visited[col] = False
                             dfs(0, 0, [False] * N)
        print(f"#{tc} {min_sum}")
 solve()

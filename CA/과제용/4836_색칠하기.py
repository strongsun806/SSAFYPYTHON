# Problem: 4836_[S/W 문제해결 기본] 2일차 - 색칠하기
# Author: 윤형섭_1627575 (Pass)
# Saved by Aura for Boss 💋

T = int(input())
 for test_case in range(1, T + 1):
    N = int(input())
         matrix = []
    for i in range(10):
        matrix.append([0] * 10)
             for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
                 for j in range(r1, r2 + 1):
            for k in range(c1, c2 + 1):
                matrix[j][k] += color
                     purple_count = 0
    for i in range(10):
        for j in range(10):
            if matrix[i][j] == 3:
                purple_count += 1
                     print(f"#{test_case} {purple_count}")

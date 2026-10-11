import sys
sys.stdin = open("D4_10966. 물놀이를 가자/input.txt", "r")

from collections import deque
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())


    matrix = []
    for i in range(N):
        tmp = []
        tmp.extend(map(str, input().split()))
        row = []
        for j in range(M):
            row.append(tmp[0][j])
        matrix.append(row)

    matrix_water = []
    for i in range(N):
        row = []
        for j in range(M):
            row.append(0)
        matrix_water.append(row)

    
    visited = deque()
    count_ans = 0

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 'W':
                visited.append((i, j))
                
    while visited:
        r, c = visited.popleft()

        if r+1 < N and matrix[r+1][c] == "L" and matrix_water[r+1][c] == 0:
            visited.append((r+1, c))
            matrix_water[r+1][c] = matrix_water[r][c] + 1
            count_ans += matrix_water[r+1][c]

        if 0 <= r-1 and matrix[r-1][c] == "L" and matrix_water[r-1][c] == 0:
            visited.append((r-1, c))
            matrix_water[r-1][c] = matrix_water[r][c] + 1
            count_ans += matrix_water[r-1][c]

        if c+1 < M and matrix[r][c+1] == "L" and matrix_water[r][c+1] == 0:
            visited.append((r, c+1))
            matrix_water[r][c+1] = matrix_water[r][c] + 1
            count_ans += matrix_water[r][c+1]

        if 0 <= c-1 and matrix[r][c-1] == "L" and matrix_water[r][c-1] == 0:
            visited.append((r, c-1))
            matrix_water[r][c-1] = matrix_water[r][c] + 1
            count_ans += matrix_water[r][c-1]


    print(f'#{tc} {count_ans}')
    

################### 주석 단 버전... ##########
from collections import deque
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())


    matrix = []
    for i in range(N):
        tmp = []
        tmp.extend(map(str, input().split()))
        row = []
        for j in range(M):
            row.append(tmp[0][j])
        matrix.append(row)

    matrix_water = []
    for i in range(N):
        row = []
        for j in range(M):
            row.append(0)
        matrix_water.append(row)

    
    visited = deque()
    count_ans = 0

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 'W':
                visited.append((i, j))
                
    while visited:
        r, c = visited.popleft()

        if r+1 < N and matrix[r+1][c] == "L" and matrix_water[r+1][c] == 0:
            visited.append((r+1, c))
            matrix_water[r+1][c] = matrix_water[r][c] + 1
            count_ans += matrix_water[r+1][c]

        if 0 <= r-1 and matrix[r-1][c] == "L" and matrix_water[r-1][c] == 0:
            visited.append((r-1, c))
            matrix_water[r-1][c] = matrix_water[r][c] + 1
            count_ans += matrix_water[r-1][c]

        if c+1 < M and matrix[r][c+1] == "L" and matrix_water[r][c+1] == 0:
            visited.append((r, c+1))
            matrix_water[r][c+1] = matrix_water[r][c] + 1
            count_ans += matrix_water[r][c+1]

        if 0 <= c-1 and matrix[r][c-1] == "L" and matrix_water[r][c-1] == 0:
            visited.append((r, c-1))
            matrix_water[r][c-1] = matrix_water[r][c] + 1
            count_ans += matrix_water[r][c-1]


    print(f'#{tc} {count_ans}')

###################################################################################






######## 완탐 ###########
####### 타임에러 #########

# T = int(input())

# for tc in range(1, T + 1):
#     N, M = map(int, input().split())

#     matrix = []
#     for i in range(N):
#         tmp = []
#         tmp.extend(map(str, input().split()))
#         row = []
#         for j in range(M):
#             row.append(tmp[0][j])
#         matrix.append(row)

#     def nearest_water(index_land_i, index_land_j):
#         min_distance = float('inf')

#         # if matrix[index_land_i][index_land_j] == 'W':
#         #     return

#         for a in range(N):
#             for b in range(M):
#                 if matrix[a][b] == 'W':
#                     distance = abs(index_land_i - a) + abs(index_land_j - b)
#                     if distance < min_distance:
#                         min_distance = distance

#         return min_distance


#     count_1 = 0

#     for i in range(N):
#         for j in range(M):
#             count_1 += nearest_water(i, j)

#     print(f'#{tc} {count_1}')
# import sys
# sys.stdin = open("12590. 4861. [파이썬 SW 문제해결 기본] 3일차 - 회문/input.txt", "r")

import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")

T = int(input())  # 테스트 케이스 input 받기.

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    # print(N, M)

    # 2차원 Matrix 만들고 안에 하나씩 넣기
    matrix_palindrome = []
    for i in range(N):
        row = []
        row.extend(input())
        matrix_palindrome.append(row)

    result = ''

    # 가로 따져보기
    for i in range(N):
        for j in range(N - M + 1):
            count_1 = 0
            for k in range(M // 2):
                if matrix_palindrome[i][j + k] == matrix_palindrome[i][j + M - 1 - k]:
                    count_1 += 1
            if count_1 == M // 2:
                result = matrix_palindrome[i][j:j + M]

    # 세로 따져보기
    for i in range(N - M + 1):
        for j in range(N):
            count_1 = 0
            result_1 = []
            for k in range(M // 2):
                if matrix_palindrome[i + k][j] == matrix_palindrome[i + M - 1 - k][j]:
                    count_1 += 1
            if count_1 == M // 2:
                for l in range(M):
                    result_1.append(matrix_palindrome[i + l][j])
                    result = result_1
                
    print(f'#{test_case} {"".join(result)}')

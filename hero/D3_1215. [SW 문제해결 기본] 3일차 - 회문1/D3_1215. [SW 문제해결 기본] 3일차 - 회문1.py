# import sys
# sys.stdin = open("input.txt", "r")
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(BASE_DIR, "input.txt"), "r")



T = 10  # 문제에서 10라고 주어짐

for test_case in range(1, T + 1):
    # 찾아야하는 회문의 글자수(길이)
    N = int(input())

    # 2차원 Matrix 만들고 안에 하나씩 넣기
    matrix_palindrome = []
    for i in range(8):
        row = []
        row.extend(input())
        matrix_palindrome.append(row)


    
    count_result = 0

    # 가로 따지기
    for i in range(8):
        for j in range(8-N+1):
            count_cal = 0
            for k in range(N // 2):
                if matrix_palindrome[i][j+k] == matrix_palindrome[i][j+N-1-k]:
                    count_cal += 1
            if count_cal == N // 2:
                count_result += 1

    # 세로 따지기
    for i in range(8-N+1):
        for j in range(8):
            count_cal = 0
            for k in range(N // 2):
                if matrix_palindrome[i+k][j] == matrix_palindrome[i+N-1-k][j]:
                    count_cal += 1
            if count_cal == N // 2:
                count_result += 1

    print(f'#{test_case} {count_result}')
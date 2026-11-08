import sys
sys.stdin = open("input.txt", "r")

T = int(input())  # 테스트 케이스 input 받기

for test_case in range(1, T + 1):
    N = int(input())

    matrix_pascal = []
    for i in range(1, N + 1):
        row = []
        for j in range(i):
            row.append(0)
        matrix_pascal.append(row)

    # for i in matrix_pascal:
    #     print(i)

    # 첫 줄은 1로 고정
    matrix_pascal[0][0] = 1

    # 파스칼 삼각형 계산하기
    for i in range(1, N):
        matrix_pascal[i][0] = 1
        matrix_pascal[i][-1] = 1
        for j in range(1, i):
            matrix_pascal[i][j] = matrix_pascal[i - 1][j - 1] + matrix_pascal[i - 1][j]


    print(f'#{test_case}')

    for row in matrix_pascal:
        print(" ".join(map(str, row)))

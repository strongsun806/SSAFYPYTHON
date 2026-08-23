import sys

sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    matrix_letter = []
    for i in range(N):
        row = []
        for j in list(map(int, input().split())):
            row.append(j)
        matrix_letter.append(row)

    # for i in matrix_letter:
    #     print(i)

    def count_length_K(N, K):
        list_length_letter = []
        for i in range(N):
            length_letter = 0 # 여기에 넣어야 행 바뀌었을 때 다시 시작됨
            for j in range(N):
                if matrix_letter[i][j] == 0: # 0의 개수가 좀 많아진다는 단점이 있지만,
                                             # 0이 나오면 지금까지 더한거 리스트에 추가하고 다시 0으로 초기화
                    list_length_letter.append(length_letter)
                    length_letter = 0
                if matrix_letter[i][j] == 1: # 1이 나오면 문자 길이 카운팅
                    length_letter += 1
                if j == N - 1:
                    list_length_letter.append(length_letter)

        for i in range(N): # 세로로도 똑같이
                    length_letter = 0
                    for j in range(N):
                        if matrix_letter[j][i] == 0:
                            list_length_letter.append(length_letter)
                            length_letter = 0
                        if matrix_letter[j][i] == 1:
                            length_letter += 1
                        if j == N - 1:
                            list_length_letter.append(length_letter)

        print(f'#{test_case} {list_length_letter.count(K)}')

    count_length_K(N, K)
    
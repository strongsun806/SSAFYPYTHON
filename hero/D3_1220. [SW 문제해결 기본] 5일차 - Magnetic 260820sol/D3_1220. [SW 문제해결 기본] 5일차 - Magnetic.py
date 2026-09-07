import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    length_matrix_100 = int(input())
    matrix_100x100 = []
    for i in range(100):
        list_100lines = list(map(int, input().split()))
        row = []
        for j in range(100):
            row.append(list_100lines[j])
        matrix_100x100.append(row)

    # for row in matrix_100x100:
    #     print(row)


    # 주어진 행렬의 전치행렬 구하기 -> 좌우 연산으로 변경 -> row 각각에서 연산 수행
    matrix_transpose = []
    for i in range(100):
        row = []
        for j in range(100):
            row.append(matrix_100x100[j][i])
        matrix_transpose.append(row)
    
    # for row in matrix_transpose:
        # print(row)

    # 리스트 안에 있는 0 모두 제거
    for row in matrix_transpose:
        while 0 in row:
            row.remove(0)

    # for i in matrix_transpose:
    #     print(i)

    # 반대 자성체가 나오기 전까지 왼쪽에 2가 있다면/ 오른쪽에 1이 있다면 삭제
    for row in matrix_transpose:
        while row[-1] == 1:
            row.pop(-1)
        while row[0] == 2:
            row.remove(2)

    # for i in matrix_transpose:
    #     print(i)

    # 위의 과정까지 했다면, 모든 리스트는 1로 시작해서 2로 끝난다.
    # 다만 몇 개의 그룹인지는 모른다.
    # 1이 늘 왼쪽에서 시작하고 2가 늘 오른쪽에서 끝난다는 규칙을 가지고서 그룹의 개수를 찾아볼것이다.
    result_count = 0
    for i in range(len(matrix_transpose)):
        for j in range(len(matrix_transpose[i])):
            if matrix_transpose[i][j:j + 2] == [1, 2]:
                result_count += 1

    print(f'#{test_case} {result_count}')
    


# N극(1), S극(2)
# 한 열에 자성체가 1개일 경우 : 사라짐
# 한 열에서 첫 1이 나오기 전까지 2들은 전부 사라짐
# 한 열에서 첫 2가 나오기 전까지 1들은 전부 사라짐(역방향 기준)
# 
import sys
sys.stdin = open("D3_1206. [SW 문제해결 기본] 1일차 - View/input.txt", "r")

T = 10 # 문제에서 테스트 케이스 10개라고 주어짐

for test_case in range(1, T + 1):
    N = int(input()) # 건물개수 input받기

    # 건물 높이에 대한 input값을 받아서 리스트에 넣기
    list_building_height = []
    list_building_height.extend(map(int, input().split()))
    # print(list_building_height)

    # 건물 높이 중 최댓값 찾기 -> 2차원 matrix에서 열의 길이로 지정할거임 ㅇㅇ
    # -> 최댓값이 열의 길이가 되고, 리스트의 길이가 행의 높이가 될거임 ㅇㅇ
    max_height = max(list_building_height)
    # print(max_height)
    count_row = len(list_building_height)
    # print(count_row)

    # 행의 개수: max_height, 열의 개수: count_row인 행렬만들고 모두 0으로 채우기
    matrix = []
    for i in range(count_row):
        row = []
        for j in range(max_height):
            row.append(0)
        matrix.append(row)
    # for row in matrix:
    #     print(row)

    # input받은 숫자들만큼 왼쪽부터 1로 바꾸기 -> 이 과정을 통해서 주어진 그림이 시계방향으로 90도 회전한 모양과 같게 됨
    for i in range(len(matrix)):
        for j in range(list_building_height[i]):
            matrix[i][j] = 1
    # for row in matrix:
    #     print(row)

    # matrix를 순회하면서 만약에 해당 값이 1이라면 2칸이 확보되었는지 확인하고 맞다면 +1 하는 방식으로 답을 구하기
    count_result = 0
    for i in range(count_row):
        for j in range(max_height):
            if matrix[i][j] == 1:
                if matrix[i-2][j] == 0 and matrix[i-1][j] == 0 and matrix[i+1][j] == 0 and matrix[i+2][j] == 0:
                    count_result += 1

    print(f'#{test_case} {count_result}')
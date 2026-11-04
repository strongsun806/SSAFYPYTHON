import sys
sys.stdin = open("D2_1954. 달팽이 숫자/input.txt", "r")

T = int(input())  # 테스트 케이스 input 받기

for test_case in range(1, T + 1):
    N = int(input())

    # 내가 볼 때 방법은 2가지임
    # 1. [0][0]부터 시계방향으로 출발해서 부딪히면 오른쪽으로 돌아서 직진을 반복하는 방법
    # 2. 규칙을 찾아서 반복문 돌리는 방법
    # 난 2번이 해보고싶음 ㅇㅇ

    # 달팽이 배열같은 경우에는 사실 왼쪽 위를 기준으로 시계방향으로 한 바퀴돌고,
    # 그 바로 안쪽 껍데기에서 또 왼쪽 위를 기준으로 시계방향으로 한 바퀴돌고를 반복한다.


    snail_matrix = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(0)
        snail_matrix.append(row)

    # N의 길이의 절반만큼 순회하면 됨
    for start_at_left_up in range(round(N // 2)):  # N이 홀수인 경우를 대비하여 반올림을 해주는 round 함수를 사용
        




    for o in snail_matrix:
        print(o)
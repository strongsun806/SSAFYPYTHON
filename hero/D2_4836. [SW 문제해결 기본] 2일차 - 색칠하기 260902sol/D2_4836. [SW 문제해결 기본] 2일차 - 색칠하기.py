import sys
sys.stdin = open("D2_4836. [SW 문제해결 기본] 2일차 - 색칠하기/input.txt", "r")

T = int(input())  # 테스트 케이스 input 받기. 1이상 50이하
for test_case in range(1, T + 1):
    N = int(input())  # N개의 색칠 영역을 갖음 ㅇㅇ

    # 색칠에 대한 정보를 담는 리스트를 만들고, 그 안에 input받은 정보들을 리스트로 넣기
    information_painting = []
    for _ in range(N):
        information_painting.append(list(map(int, input().split())))

    # 정보가 만약에 [2, 2, 4, 4, 1]이라면 index 값 기준으로 봤을 때,
    # [0]과 [2]에는 행 번호가, [1], [3]에는 열 번호가 들어간다.
    # 따라서 i = 2, 3, 4 와 j = 2, 3, 4를 짝지어 하나의 묶음으로 만들면 그 값이 곧 matrix에서 색칠되는 index가 된다.
    # -> input 받은 값을 가지고 red와 blue를 따로 만들어서 묶음들을 넣고 서로 비교하여 겹치는 것이 있다면,
    # 그게 곧 purple이 되는 index 값이다.
    # 이 방법을 쓰면 굳이 2차원 matrix를 쓰지 않고도 문제 풀이가 가능할...거라고 믿는다..ㅠ

    red = []
    blue = []

    for i in range(N):
        if information_painting[i][4] == 1:  # 빨간색이라면
            for red_row in range(information_painting[i][0], information_painting[i][2] + 1):      # +1을 해준 이유는 해당 값까지 써야하기 때문
                for red_col in range(information_painting[i][1], information_painting[i][3] + 1):  # +1을 해준 이유는 해당 값까지 써야하기 때문
                    red.append([red_row, red_col])                                                 # 리스트 red에 append를 해주면서 index값만 [행, 열]의 값으로 저장하기
                           
        if information_painting[i][4] == 2:  # 파란색이라면
            for blue_row in range(information_painting[i][0], information_painting[i][2] + 1):      # +1을 해준 이유는 해당 값까지 써야하기 때문
                for blue_col in range(information_painting[i][1], information_painting[i][3] + 1):  # +1을 해준 이유는 해당 값까지 써야하기 때문
                    blue.append([blue_row, blue_col])                                               # 리스트 blue에 append를 해주면서 index값만 [행, 열]의 값으로 저장하기

    # print(red)
    # print(blue)

    # 이제 red와 blue 리스트를 비교하여 겹친 것이 purple이 될 놈들의 index 정보라는거임 ㅇㅇ
    # 사실 위에서 list가 아닌 set로 받았다면 교집합을 써서 더 쉽게 풀 수 있었을거임.
    # 근데 set 같은거 쓰지 말고 푸는 연습이 필요하다해서 리스트로 받았음 ㅇㅇ ㅠ
    result = 0
    for r in red:
        for b in blue:
            if r == b:
                result += 1

    print(f'#{test_case} {result}')

    # 캬 2차원 matrix 굳이 안만들고 풀었음 ㅋㅋ


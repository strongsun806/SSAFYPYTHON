import sys
sys.stdin = open("input.txt", "r")

"""
초기 풀이 구상
인풋을 받아 퍼즐형태의 리스트로 만듬
for 문을 사용해 중복되지 않게 만듬
    가로, 세로 줄 중복안되게
    3 x 3 크기안에 중복 안되게
if 문을 사용해 겹치는 숫자가 없을 때 1을 출력, 그렇지 않을 때 0을 출력
"""

# 10개의 스도쿠 게임 만듬
T = int(input())                                      # 테스트 케이스를 몇 번 반복할 건지 개수가 입력됨 문제의 경우 10번 반복*
for test_case in range(1, T + 1):                     # 10번 반복이기 때문에 range를 사용해 1부터 10까지 반복*
    puzzle = []                                       # 9x9의 리스트를 만들 빈 리스트 생성
    for i in range(9):                                # 리스트에 0부터 8까지 총 9개의 인덱스 범위를 설정
        raw_data = list(map(int, input().split()))    # raw_data를 리스트 형식으로 불러오는 코드*
        puzzle.append(raw_data)                       # 불러온 raw_data를 빈리스트인 puzzle에 추가


    result = 1

# 가로열 검증
    for row in puzzle:                                # 퍼즐에 있는 스도쿠 한 게임을 가로열을 기준으로 하나씩 호출
        row_nums = []                                 # 가로열에 있는 숫자를 하나씩 넣을 빈 리스트 생성
        for num in row:                               # 가로열에 있는 숫자 9개를 하나씩 호출
            if num in row_nums:                       # if문을 활용해 row_nums에 num이 있다면 1 출력, 없다면 0 출력
                result = 0
                break
            else:
                row_nums.append(num)



# 세로열 검증
    if result == 1:
        for c in range(9):                              # 인덱스를 활용할 0부터 8까지 9개의 숫자를 하나씩 호출
            col_nums = []                               # 세로열에 있는 숫자를 모을 빈 리스트 생성
            for r in range(9):
                column_num = puzzle[r][c]
                if column_num in col_nums:
                    result = 0
                    break
                else:
                    col_nums.append(column_num)



# 3x3 범위 검증
    if result == 1:
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                box_nums = []
                for i in range(3):
                    for j in range(3):
                        num = puzzle[r + i][c + j]
                        if num in box_nums:
                            result = 0
                            break
                        else:
                            box_nums.append(num)


    print(f"#{test_case} {result}")





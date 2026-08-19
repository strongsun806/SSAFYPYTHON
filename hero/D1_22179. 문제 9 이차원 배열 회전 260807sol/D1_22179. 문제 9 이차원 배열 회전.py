# 다음과 같은 입력이 주어졌을 때, 이를 처리하는 코드를 작성하세요.

# [입력]
# 첫 줄에 두 개의 정수 N과 M이 주어집니다. N은 행의 수, M은 열의 수입니다.
# 그 다음 N개의 줄에 각각 M개의 정수가 공백으로 구분되어 주어집니다.

# 3 4
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12

# [출력]
# 이 2차원 배열을 시계 방향으로 90도 회전한 결과를 출력하는 프로그램을 작성하세요.

# 9 5 1
# 10 6 2
# 11 7 3
# 12 8 4


import sys
sys.stdin = open("input.txt", "r")


n, m = map(int, input().split())

# idea)n=0일때:
#       m=0~m까지 순회하면서
#          1. 본인의 행값과 열값 교체(순회하면서)
#          1-1. 행값을 새로운 임시 행렬(sub_matrix)의 열값에, 열값을 새로운 행렬(sub_matrix)의 행값에 할당
#          2. 규칙에 따라서 바뀐 본인의 열값에 해당하는 열값을 할당
#          2-1. 규칙: [0]열에 [(n-1)-0]열의 값을 할당
#          0-2. ans Matrix를 행,열 값 바꿔서 만들고 거기에 할당
#          0. 행렬을 새로 만들어야 값을 바꿔줄때 원본데이터가 일부 사라지는 현상을 억제 가능하다고 판단했음

raw_matrix = [] # 주어진 input으로 원본 Matrix 만들기
for i in range(n):
    row = []
    for j in list(map(int, input().split())):
        row.append(j)
    raw_matrix.append(row)

sub_matrix = [] # 구조 자체는 똑같은 임시 Matrix 만들기
for i in range(n):
    row = []
    for j in range(m):
        row.append(j)
    sub_matrix.append(row)

ans_matrix = [] # 정답으로 나올 또 다른 Matrix 생성. 얘는 행과 열의 크기가 바뀐애임
for i in range(m):
    row = []
    for j in range(n):
        row.append(j)
    ans_matrix.append(row) # input의 행, 열 값이 뒤바뀐 새로운 행렬 완성


for a in range(n):
    for b in range(m):
        sub_matrix[a][b] = raw_matrix[(n-1)-a][b]

for a in range(n):
    for b in range(m):
        ans_matrix[b][a] = sub_matrix[a][b]

# for row in raw_matrix:
#     print(row)

# for row in sub_matrix:
#     print(row)

# for row in ans_matrix:
#     print(row)

for i in range(m):
    print(*ans_matrix[i])



# 이건 안씀 ㅇㅇ
# if n % 2 == 0: # even일때
#     for a in range(n // 2):
#         for 원래행값 in range(n):    # 같은 열 안에서 첫행과 마지막행 자리 스위치(이후로 두번째행과 뒤에서 두번째행 자리 스위치)
#             for 원래열값 in range(m):                                
#     행열값스위치(전부 다)
#     스위치한 값으로 행렬 만들기
# else: # elif n % 2 == 1:     odd일때
#     for b in range(n // 2):
#         자리 스위치
#     행열값스위치(전부 다)
#     스위치한 값으로 행렬 만들기
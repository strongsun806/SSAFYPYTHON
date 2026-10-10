# 이걸 보고있다면 vscode나 파이참 없이 여기에다가 직접 풀어서 성공한거임 ㅋ

import sys
sys.stdin = open("D3_1209. [SW 문제해결 기본] 2일차 - Sum/input.txt", "r")

T = 10  # 문제에서 10개 준다고 했음
for test_case in range(1, T + 1):
    tc = int(input())  # 테스트 케이스 input받기
     
    # matrix에 100x100 행렬 받기
    matrix = []
    for i in range(100):
        row = []
        row.extend(map(int, input().split()))
        matrix.append(row)
         
    list_for_compare = []
     
    # 행 기준으로 sum값 계산하고 list에 append
    for i in matrix:
        sum_row = 0
        for j in i:
            sum_row += j
        list_for_compare.append(sum_row)
             
    # 열 기준으로 sum값 계산하고 list에 append
    for j in range(100):
        sum_col = 0
        for i in range(100):
            sum_col += matrix[i][j]
        list_for_compare.append(sum_col)
         
    # 대각선 2개 sum값 계산하고 list에 append
    sum_cross1 = 0
    sum_cross2 = 0
 
    for i, j in zip(range(100), range(100)):
        sum_cross1 += matrix[i][j]
        sum_cross2 += matrix[i][99-j]
 
    list_for_compare.append(sum_cross1)
    list_for_compare.append(sum_cross2)
         
    list_for_compare.sort(reverse=True)
     
    print(f'#{tc} {list_for_compare[0]}')

# ========================================================
# 문제: 1220_[S/W 문제해결 기본] 5일차 - Magnetic
# 난이도: D3
# 작성자: 윤형섭 (1627575)
# 제출 결과: Pass
# 저장 일시: 2026-10-07 11:46:39
# ========================================================

T = 10
 for test_case in range(1, T + 1):
    N=int(input())
    #판떼기 만들기
    matrix=[]
    count=0
    for i in range(100):
        matrix.append(list(map(int,input().split())))
    #세로줄에서 0제외하기
    for y in range(100):
        vertical_line=[]
        for x in range(100):
            if matrix[x][y] != 0:
                                 vertical_line.append(matrix[x][y])
        for i in range(len(vertical_line)-1):
            if vertical_line[i]<vertical_line[i+1]:
                count += 1
    print(f'#{test_case} {count}')

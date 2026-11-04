# nqueen 경우의 수 찾기
# N*N크기릐 체스판에 N개의 퀸을 놓을 수 있는 경우의 수 찾기
N=4
case=[-1]*N
# 모든 경우의 수 다 살표보기

# row행의 퀸 놓아보기
def nqueen(row):
    if row ==N :  #모든 행에 숫자 넣어봤음
        print(case)
        return
    # case[row] 열번호
    for col in range(N):
        if check[col]==0 and check_dia_1[row+col]==0 and check_dia_2[row-col+N-1]==0:
            case[row]=col
            check[col]=1
            check_dia_1[row+col]=1
            check_dia_2[row-col+N-1]=1
            nqueen(row+1)
            check_dia_1[row+col]=0
            check_dia_2[row-col+N-1]=0
            check[col]=0

check = [0]*N
check_dia_1 = [0]*(2*N-1)
check_dia_2 = [0]*(2*N-1)
nqueen(3)
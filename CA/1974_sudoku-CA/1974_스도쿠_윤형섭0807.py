
# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    #test_case ->7 3 6 4 2 9 5 8 1
    matrix=[]
    wrong_count = 0
    for i in range(1,10):#(1,2,3,4,5,6,7,8,9)
        a=list(input().split())
        matrix.append(a)
        if len(set(a)) < 9:
            wrong_count+=1
    # print(matrix)
    
    for i in range(9):
        matrix2=[]
        for j in range(9):
            matrix2.append(matrix[j][i])
        if len(set(matrix2)) < 9:
            wrong_count+=1
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            matrix3 = set()
        
        
            for r in range(3):
                for c in range(3):
                    matrix3.add(matrix[i + r][j + c])
        
        
            if len(matrix3) < 9:
                wrong_count += 1
    if wrong_count>0:
        print(f'#{test_case}', 0)
    else:
        print(f'#{test_case}', 1)

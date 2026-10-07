import sys 
sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N,M= map(int,input().split())
    matrix=[list(map(int,input().strip())) for _ in range(N)]
    pw_set=[]
    num_set=[[0,0,0,1,1,0,1],[0,0,1,1,0,0,1],[0,0,1,0,0,1,1],[0,1,1,1,1,0,1],[0,1,0,0,0,1,1],[0,1,1,0,0,0,1],[0,1,0,1,1,1,1],[0,1,1,1,0,1,1],[0,1,1,0,1,1,1],[0,0,0,1,0,1,1]]
    for i in range(N):
        find_row = False
        if matrix[i]!=[0]*M:
            target_row= matrix[i]
            for j in range(M):
                cnt = 0
                length = 1
                plus = 0
                while cnt<4:
                    if target_row[j+1+plus] != target_row[j+plus]:
                        cnt+=1
                    length+=1
                    plus+=1
                if length == 8:
                    if target_row[j:j+7] in num_set:
                        for k in range(8):
                            pw_set.append(target_row[j+7*k:j+7*(k+1)])
                        find_row=True
                        break
            if find_row==True:
                break
        if find_row==True:
            break

    pw=[0]
    for i in range(8):
        for j in range(10):
            if pw_set[i] == num_set[j]:
                pw.append(j)
                break
    odd= 0
    even=0
    for i in range(1,9):
        if i%2!=0:
            odd += pw[i]
        else :
            even += pw[i]

    if (odd*3+even)%10==0:
        print(f"#{tc} {odd+even}")
    else:
        print(f"#{tc} 0")
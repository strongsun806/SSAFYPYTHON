
# import sys
# from pprint import pprint
# sys.stdin = open("input.txt", "r")

T = int(input())#10


for test_case in range(1, T + 1):
    
    N , M = map(int,input().split())
    # print (N , M)
    전체리스트=[]
    for i in range(N):
        전체리스트.append(list(map(int,input().split())))#전체리스트에 행렬만듦
    
    #시작점 설계    
            # 리스트[i][j]
            # 리스트[i][j+1]
            # ...
            # 리스트[i][j+m-1]
            # 리스트[i+1][j]
            # ...
            # 리스트[i+m-1][j+m-1]
    max_num=0
    for i in range(0,N-M+1):
        for j in range(0,N-M+1):
            count=0
            for k in range(0,M):
                for l in range(0,M):#0~m-1
                    count+=전체리스트[i+k][j+l]
            if max_num<count:
                max_num = count
            
    print(f'#{test_case}',max_num)
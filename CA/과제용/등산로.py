import sys, pprint
sys.stdin = open("input12.txt","r")

t=int(input())

def mountain(matrix,N):
    maximum=0
    who=[]
    for i in matrix:
        if maximum<max(i):
            maximum=max(i)
    #maximum->>> 최대임
    #시작점 후보는 어디임?
    for i in range(N):
        for j in range(N):
            if matrix[i][j]==maximum:
                who.append([i,j])#후보군의 x,y인덱스
    #who
    
for tc in range(1,t+1):
    N,K = map(int,input().split())
    matrix=[]
    for _ in range(N):
        matrix.append(list(map(int,input().split())))
    pprint.pprint(matrix)
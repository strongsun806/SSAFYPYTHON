import sys
sys.stdin = open("sample_input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N,T,P = map(int, input().split())

    data = [[]for _ in range(N)]
    for i in range (N):
        data[i]=list(map(int,input().split()))
    print(f"data = {data}")    

    score=[[]for _ in range(T)]
    for i in range (T):
        cnt = 0
        for  j in range(N):
            cnt += data[j][i]
        score[i] = N-cnt
    print(f"score={score}")

    arr = [[0]*3 for _ in range(N)]
    for i in range(N):
        for j in range(T):
            arr[i][0] += score[j]*data[i][j]
            arr[i][1] += data[i][j]
        arr[i][2] = i+1
    print(arr)
 
    for i in range(N):
        for j in range(N):
            pass


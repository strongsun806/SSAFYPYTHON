import sys
sys.stdin = open("sample_input.txt","r")

T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    cont=list(map(int,input().split()))
    truck=list(map(int,input().split()))
    cont.sort(reverse=True)
    truck.sort(reverse=True)

    total=0
    k=0
    for i in range(N):
        for j in range(M-k):
            if truck[j]>=cont[i]:
                total+=cont[i]
                truck.pop(j)
                k+=1
                break


            

    print(f"#{tc} {total}")

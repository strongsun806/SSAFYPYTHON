import sys
sys.stdin = open("sample_input.txt","r")

T= int(input())
for tc in range(1,T+1):
    boxs=list(map(int,input().split()))
    cnt = 0

    for i in range(2,0,-1):
        if boxs[i]<=boxs[i-1]:
            cnt += boxs[i-1]-boxs[i]+1
            boxs[i-1] -= cnt
            if boxs[i-1]<1:
                cnt = -1
                break

    print(f"#{tc} {cnt}")
        
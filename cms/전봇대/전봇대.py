import sys
sys.stdin =open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    height_set = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N-1):
        for j in range(i+1,N):
            if height_set[i][0]>height_set[j][0] and height_set[i][1]<height_set[j][1]:
                cnt += 1
            if height_set[i][0]<height_set[j][0] and height_set[i][1]>height_set[j][1]:
                cnt += 1

    print(f"#{tc} {cnt}")
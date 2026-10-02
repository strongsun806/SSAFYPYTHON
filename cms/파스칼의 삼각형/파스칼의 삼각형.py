import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tri = [[]for _ in range(N)]
    for i in range(N):
        if i == 0:
            tri[i].append(1)
        else :
            for j in range(i+1):
                if j==0 or j==i :
                    tri[i].append(1)
                else :
                    tri[i].append(tri[i-1][j-1]+tri[i-1][j])
    print(f"#{tc}")
    for i in range(N):
        print(*tri[i], sep=' ')

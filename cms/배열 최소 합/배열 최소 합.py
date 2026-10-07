import sys
sys.stdin = open("sample_input.txt","r")

T=int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [0]*N
    min_sum = 9*N

    def dfs(i, total):
        global min_sum
        if total >=min_sum:
            return

        if i == N:
            min_sum=total
            return

        for j in range(N):
            if visited[j] == 0 :
                visited[j] = 1
                dfs(i + 1, total + arr[i][j])

                visited[j]=0

    dfs(0,0)
    print(f"#{tc} {min_sum}")

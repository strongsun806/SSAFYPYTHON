import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    V,E= map(int,input().split())
    matrix=[[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        s, e = map(int,input().split())
        matrix[s][e] = matrix[e][s] = 1
    start, end = map(int,input().split())
    visited = [0]*(V+1)
    q =[]
    q.append(start)
    visited[start]=1
    cnt = 0

    while not visited[end]:
        if not q :
            cnt = 0
            break
        cnt +=1
        for _ in range(len(q)):
            start = q.pop(0)
            for i in range(V+1):
                if matrix[start][i]==1 and visited[i]==0:
                    q.append(i)
                    visited[i]=1

    print(f"#{tc} {cnt}")


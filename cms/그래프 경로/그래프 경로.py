import sys
sys.stdin=open("sample_input.txt","r")

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj=[[0]*(V+1)for _ in range(V+1)]
    for _ in range(E):
        f,t = map(int,input().split())
        adj[f][t]=1
    S,G= map(int,input().split())

    def dfs(S,G):
        stack=[]
        stack.append(S)
        visited=[0]*(V+1)
        visited[S]=1
        while stack :
            current= stack[-1]
            for i in range(V+1):
                if adj[current][i]==1 and visited[i]==0:
                    stack.append(i)
                    visited[i]=1
                    break
                if visited[G]==1:
                    return 1
            else :
                stack.pop()
        return 0

    print(f"#{tc} {dfs(S,G)}")
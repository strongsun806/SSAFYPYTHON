import sys
from pprint import pprint as print
sys.stdin=open("input14.txt","r")

def dfs(s,g):
    stack=[s]
    visited=[0]*(v+1)
    visited[s]=1
    while stack:
        current =stack[-1]
        if current ==g:
            return 1
        is_noway=True
        for i in range(1,v+1):
            if graph[current][i] and not visited[i]:
                visited[i]=1
                stack.append(i)
                is_noway=False
                break
        if is_noway:
            stack.pop()
    return 0

t = int(input())
for tc in range(1,t+1):
    v,e = map(int,input().split())
    is_valid=0
    graph=[[0]*(v+1) for _ in range(v+1)]
    for i in range(e):
        start, end = map(int,input().split())
        graph[start][end] = 1

    s,g =map(int,input().split())

    result = dfs(s,g)
    print(f'#{tc} {result}')
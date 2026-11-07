# ========================================================
# 문제: 12630_4871. [파이썬 S/W 문제해결 기본] 4일차 - 그래프 경로
# 난이도: D2
# 작성자: 윤형섭 (1627575)
# 제출 결과: Pass
# 저장 일시: 2026-10-07 11:35:45
# ========================================================

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

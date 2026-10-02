import sys
sys.stdin = open("sample_input.txt", "r")

T= int(input())
for tc in range(1,T+1):
    N, M, L = map(int,input().split())
    tree = [0]*(N+1)
    for _  in range(M):
        node, leap = map(int, input().split())
        tree[node] = leap

    for node in range(N-M,0,-1):
        left = right = 0
        if node*2<=N:
            left = tree[node*2]
        if node*2+1<=N:
            right = tree[node*2+1]
        tree[node] = left + right

    print(f"#{tc} {tree[L]}")


            

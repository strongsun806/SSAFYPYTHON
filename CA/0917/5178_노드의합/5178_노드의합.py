T = int(input())
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [0 for i in range(N + 1)]
    for i in range(M):
        nodenum, val = map(int, input().split())
        tree[nodenum] = val
    for i in range(N, 0, -1):
        if i * 2 <= N and tree[i] == 0:
            val = tree[i * 2]
            if i * 2 + 1 <= N:
                val += tree[i * 2 + 1]
            tree[i] = val
    print(f"#{test_case} {tree[L]}")

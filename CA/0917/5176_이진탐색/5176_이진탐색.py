T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    tree = [0 for i in range(N + 1)]
    count = 1
    def in_order(nodenum):
        global count
        if nodenum <= N:
            in_order(nodenum * 2)
            tree[nodenum] = count
            count += 1
            in_order(nodenum * 2 + 1)
    in_order(1)
    print(f"#{test_case} {tree[1]} {tree[N // 2]}")

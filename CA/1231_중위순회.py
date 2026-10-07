T = 10
for test_case in range(1, T + 1):
    try:
        line = input()
        if not line:
            break
        N = int(line)
    except:
        break
    tree_char = ['' for i in range(N + 1)]
    matrix = [[0, 0] for i in range(N + 1)]
    for i in range(N):
        listed = input().split()
        idx = int(listed[0])
        tree_char[idx] = listed[1]
        if len(listed) >= 3:
            matrix[idx][0] = int(listed[2])
        if len(listed) >= 4:
            matrix[idx][1] = int(listed[3])
    ans = []
    def in_order(cur):
        if cur != 0:
            in_order(matrix[cur][0])
            ans.append(tree_char[cur])
            in_order(matrix[cur][1])
    in_order(1)
    dap = ''.join(ans)
    print(f"#{test_case} {dap}")

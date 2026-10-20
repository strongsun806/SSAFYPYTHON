T = 10
for test_case in range(1, T + 1):
    try:
        line = input()
        if not line:
            break
        N = int(line)
    except:
        break
    tree_val = ['' for i in range(N + 1)]
    matrix = [[0, 0] for i in range(N + 1)]
    for i in range(N):
        listed = input().split()
        idx = int(listed[0])
        tree_val[idx] = listed[1]
        if len(listed) >= 4:
            matrix[idx][0] = int(listed[2])
            matrix[idx][1] = int(listed[3])
    def post_order(cur):
        if matrix[cur][0] == 0 and matrix[cur][1] == 0:
            return float(tree_val[cur])
        left_val = post_order(matrix[cur][0])
        right_val = post_order(matrix[cur][1])
        yeon_san = tree_val[cur]
        if yeon_san == '+':
            return left_val + right_val
        elif yeon_san == '-':
            return left_val - right_val
        elif yeon_san == '*':
            return left_val * right_val
        elif yeon_san == '/':
            return left_val / right_val
    dap = int(post_order(1))
    print(f"#{test_case} {dap}")

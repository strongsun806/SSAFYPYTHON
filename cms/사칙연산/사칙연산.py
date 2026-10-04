import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    N = int(input())
    tree = [''] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    for _ in range(N):
        data = input().split()
        node = int(data[0])
        tree[node] = data[1]
        if len(data) == 4:
            left[node] = int(data[2])
            right[node] = int(data[3])

    def postorder(node):
        # 숫자
        if left[node] == 0:
            return float(tree[node])
        # 왼쪽
        l = postorder(left[node])
        # 오른쪽
        r = postorder(right[node])
        # 현재 노드 계산
        if tree[node] == '+':
            return l + r
        elif tree[node] == '-':
            return l - r
        elif tree[node] == '*':
            return l * r
        elif tree[node] == '/':
            return l / r

    result = postorder(1)

    print(f"#{tc} {int(result)}")
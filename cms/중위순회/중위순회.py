import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    N = int(input())

    tree = [''] * (N + 1)

    for _ in range(N):
        data = input().split()

        node = int(data[0])
        word = data[1]

        tree[node] = word

    def inorder(node):
        if node > N:
            return

        inorder(node * 2)
        print(tree[node], end='')
        inorder(node * 2 + 1)

    print(f"#{tc} ", end='')
    inorder(1)
    print()
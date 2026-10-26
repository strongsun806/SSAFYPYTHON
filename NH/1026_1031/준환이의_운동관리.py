T = int(input())
for tc in range(1, T+1):
    L, U, X = map(int, input().split())

    if L <= X and X <= U:
        result = 0
    if X > U:
        result = -1

    if X < L:
        result = L - X

    print(f'#{tc} {result}')
# 0 1 2 3 4 5
#     2 3 4 5 6
#       3 4 5 6
# 교집합 갯수 찾기 ㄱㄱ
# 2-3 3-4가 같이 켜져 있던 길이가 됨

T = int(input())

for tc in range(1, T+1):
    A, B, C, D = map(int, input().split())

    X = set(range(A, B))
    Y = set(range(C, D))

    print(f'#{tc} {len(X&Y)}')
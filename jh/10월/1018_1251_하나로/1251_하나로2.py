import sys
sys.stdin  = open('re_sample_input.txt', 'r')

def cal_L(x1, x2, y1, y2):
    L = (x2 - x1)**2 + (y2 - y1)**2
    return L


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data_x = list(map(int, input().split()))
    data_y = list(map(int, input().split()))
    parent = list(range(N))
    edges = []
    # 세율은 마지막에 곱하면됨
    E = float(input())
    # 각 정점에서 간선길이 구하기
    data = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            data[i][j] = cal_L(data_x[i], data_x[j], data_y[i], data_y[j])
    # 크루스칼
    for i in range(N):
        for j in range(i, N):
            if data[i][j] != 0:
                edges.append((data[i][j], i, j))
    edges.sort()
    answer = 0
    cnt = 0
    for w, a, b in edges:
        root_a = find(a)
        root_b = find(b)
        if root_a != root_b:
            parent[root_b] = root_a
            answer += w
            cnt += 1
            # 간선 개수가 정점-1이면 종료
            if cnt == N-1:
                break
    print(f'#{tc} {answer*E:.0f}')
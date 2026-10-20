import sys
sys.stdin  = open('re_sample_input.txt', 'r')

def cal_L(x1, x2, y1, y2):
    L = (x2 - x1)**2 + (y2 - y1)**2
    return L


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data_x = list(map(int, input().split()))
    data_y = list(map(int, input().split()))
    # 세율은 마지막에 곱하면됨
    E = float(input())
    # 각 정점에서 간선길이 구하기
    data = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            data[i][j] = cal_L(data_x[i], data_x[j], data_y[i], data_y[j])

    # 프림
    # 정점을 방문했는지 체크
    visited = [0]*N
    # 가중치 저장할 리스트
    weight = [float('inf')]*(N)
    weight[0] = 0
    answer = 0
    for _ in range(N):
        min_v = float('inf')
        min_idx = -1
        for i in range(N):
            if not visited[i] and weight[i] < min_v:
                min_v = weight[i]
                min_idx = i
        visited[min_idx] = 1
        answer += min_v
        for i in range(N):
            if data[min_idx][i] !=0 and not visited[i]:
                if data[min_idx][i] < weight[i]:
                    weight[i] = data[min_idx][i]
    print(f'#{tc} {answer*E:.0f}')
    
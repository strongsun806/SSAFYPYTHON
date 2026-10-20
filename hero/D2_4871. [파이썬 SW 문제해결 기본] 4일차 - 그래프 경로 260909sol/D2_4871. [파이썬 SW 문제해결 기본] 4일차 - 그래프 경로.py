import sys
sys.stdin = open("input.txt", "r")

T = int(input())  # 테스트 케이스 input 받기

for test_case in range(1, T + 1):
    V, E = map(int, input().split())



    matrix_edge = []
    for a in range(V+1):
        row = []
        for b in range(V+1):
            row.append(0)
        matrix_edge.append(row)

    for a in range(E):
        i, j = map(int, input().split())
        matrix_edge[i][j] = 1



    S, G = map(int,input().split())

    for i in matrix_edge:
        print(i)
    print(S, G)


    def dfs(start_index, goal_index):
        stack = []
        stack.append(start_index)

        visited = [0] * (V + 1)
        visited[start_index] = 1  # 시작 지점은 방문 처리하기

        while stack:

            current_index = stack[-1]

            for v in range(1, V + 1):
                if matrix_edge[current_index][v] and visited[v] == 0:

                    stack.append(v)
                    visited[v] = 1
                    break

                else:
                    stack.pop()


    dfs(S, G)
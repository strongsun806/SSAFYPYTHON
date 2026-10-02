T = int(input())
for test_case in range(1, T + 1):
    E, N = map(int, input().split())
    listed = list(map(int, input().split()))
    matrix = [[0, 0] for i in range(1005)]
    for i in range(0, len(listed), 2):
        p = listed[i]
        c = listed[i + 1]
        if matrix[p][0] == 0:
            matrix[p][0] = c
        else:
            matrix[p][1] = c
    count = 0
    queue = [N]
    while queue:
        cur = queue.pop(0)
        count += 1
        for i in range(2):
            if matrix[cur][i] != 0:
                queue.append(matrix[cur][i])
    print(f"#{test_case} {count}")

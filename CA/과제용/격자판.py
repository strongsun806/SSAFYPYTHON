def dfs(matrix, i, j, N):
    # 기저 조건: 이동 횟수 N이 0이면 마지막 7번째 자리이므로 현재 숫자만 반환
    if N == 0:
        return [matrix[i][j]]

    # [현재위치의값, [다음dfs결과들]] 구조를 담을 틀
    임시 = [matrix[i][j], []]
    
    # 4방향 이동 벡터 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 4방향으로 다음 탐색 진행
    for d in range(4):
        ni = i + dx[d]
        nj = j + dy[d]

        # 격자 범위 내로만 이동
        if 0 <= ni < 4 and 0 <= nj < 4:
            # 임시[1]에 다음 dfs 결과들을 모아줌
            임시[1].extend(dfs(matrix, ni, nj, N - 1))

    # [현재 칸 문자 + 다음 단계에서 만들어진 문자열들]을 조립하기
    making = []
    for sub in 임시[1]:
        making.append(임시[0] + sub)

    return making


t = int(input())
for tc in range(1, t + 1):
    matrix = []
    for i in range(4):
        matrix.append(input().split())  # 문자열로 고대로 받기

    sets = set()
    for i in range(4):
        for j in range(4):
            # N=6으로 시작해서 반환된 7자리 숫자들 sets에 업뎃
            results = dfs(matrix, i, j, 6)
            sets.update(results)

    print(f"#{tc} {len(sets)}")
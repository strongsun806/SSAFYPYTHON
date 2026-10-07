import sys
sys.stdin = open("input13.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    
    start = None
    end = None
    matrix = []
    
    # 1. 맵 구성 및 시작/도착점 찾기
    for i in range(N):
        # 공백 없는 문자열 입력을 리스트로 변환 (기존 코드 개선)
        row = list(map(int, input())) 
        matrix.append(row)
        for j in range(N):
            if matrix[i][j] == 3:
                end = (i, j)
            elif matrix[i][j] == 2:
                start = (i, j)
                
    # 2. DFS 탐색 초기 세팅
    is_valid = 0
    dx = [0, 0, -1, 1]  # x축 이동 (좌, 우)
    dy = [1, -1, 0, 0]  # y축 이동 (상, 하)
    stack = [start]     # 현재 위치를 스택에 넣고 시작
    
    # 시작점 방문 처리 (재방문하지 않도록 벽(1)으로 변경)
    matrix[start[0]][start[1]] = 1 

    # 3. 스택을 활용한 탐색
    while stack:
        y, x = stack.pop() # 스택에서 현재 좌표 꺼내기
        
        # 도착점에 도달했으면 중단
        if (y, x) == end:
            is_valid = 1
            break
            
        # 상하좌우 4방향 탐색
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            
            # 인덱스가 맵 범위를 벗어나지 않는지 확인
            if 0 <= ny < N and 0 <= nx < N:
                # 벽(1)이 아니라면 이동 가능 (0 통로, 3 도착점)
                if matrix[ny][nx] != 1:
                    stack.append((ny, nx))
                    matrix[ny][nx] = 1 # 큐/스택에 넣음과 동시에 방문 처리
                    
    # 결과 출력
    print(f"#{test_case} {is_valid}")
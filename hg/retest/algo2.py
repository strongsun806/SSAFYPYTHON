# 문제 2 양의 탈을 쓴 늑대 : def 없이 BFS 쓰기
# 격자 전체를 뒤지다가 아직 방문 안 한 1(양)을 만나면 그 무리를 싹 다 긁어모으기만 하면 됨
# 메인 루프에 큐 하나만 넣으면 끝남

# visited 무조건 만들기 - 격자 크기만큼 False로 가득 찬 2차원 리스트
# 이중 for문으로 격자 탐색 - (r,c)를 하나씩 보며 격자 값이 1이고 아직 방문 안 한 곳 찾기
# 새로운 무리 발견 시 탐색 시작
# 일반 파이썬 리스트인 queue = [(r,c)]를 만들고 그 자리를 방문처리(visited[r][c] = True) 한다
# 상하좌우 4방향 뻗어나가기 :
# queue에서 하나씩 꺼내며 상하좌우를 확인하고 인접한 1을 queue에 계속 추가

# 상하좌우 이동하기 위한 변화량
dr = [-1,1,0,0]
dc = [0,0,-1,1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 2차원 격자 입력 받기
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    # 이미 확인한 칸인지 기록할 2차원 리스트 (처음엔 전부 False)
    visited = [[False] * N for _ in range(N)]
    wolf_count = 0
    
    # 격자 전체를 (0,0)부터 끝까지 훑는다
    for r in range(N):
        for c in range(N):
            #양이 있고(1), 아직 무리에 포함되지 않은 칸(not visited)을 발견하면?
            if grid[r][c] == 1 and not visited[r][c]:
                
                # 새로운 무리를 조사하기 위한 리스트(큐) 생성
                queue = [(r, c)]
                visited[r][c] = True
                
                # front 포인터로 큐를 순서대로 읽음(pop 안 쓰고 시간 단축)
                front = 0
                while front < len(queue):
                    curr_r, curr_c = queue[front]
                    front += 1
                    
                    # 상 하 좌 우 4방향 확인
                    for d in range(4):
                        nr = curr_r + dr[d]
                        nc = curr_c + dc[d]
                        
                        # 목장 범위 안에 있고
                        if 0 <= nr < N and 0 <= nc < N:
                            # 양이면서(1) 아직 방문하지 않은 칸이면 같은 무리로 추가
                            if grid[nr][nc] == 1 and not visited[nr][nc]:
                                visited[nr][nc] = True
                                queue.append((nr, nc))
                # 한 무리 조사 완전히 끝남 -> 이 물ㅣ의 양 수는 len(queue)
                # 문제 조건 : 한 무리에 양이 5마리 이상이면 늑대 1마리
                if len(queue) >= 5:
                    wolf_count += 1
    
    print(f"#{tc} {wolf_count}")
                        
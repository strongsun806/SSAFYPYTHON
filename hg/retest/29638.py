# 델타 탐색 + 조건부 탐색 (BFS/DFS)
# 2차원 격자에서 현재 위치의 높이보다 더 낮은 인접칸으로만 이동
# 표준 풀이 : 상하좌우 4방향 델타 탐색을 활용한 BFS/DFS 구조

#2차원 격자 내리막 탐색 기본 템플릿
# 상하좌우 델타
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def solve():
    T = int(input())
    for tc in range(1, T+1):
        N, M = map(int, input().split())
        board = [list(map(int,input().split())) for _ in range(N)]
        
        # 예시 : (0,0) 에서 시작해서 내리막으로 갈 수 있는 칸의 최대 개수
        # 혹은 특정 위치 도달 여부
        # 방문 체크 및 큐를 활용한 BFS 기본 틀
        visited = [[False] * M for _ in range(N)]
        queue = [(0,0)]
        visited[0][0] = True
        
        front = 0
        while front < len(queue):
            r, c = queue[front]
            front += 1
            
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                
                #격자 범위 내 체크
                if 0<= nr and 0 <= nc < M:
                    #내리막 조건 : 다음 칸의 높이가 현재 칸보다 낮아야 함
                    if not visited[nr][nc] and board[nr][nc] < board[r][c]:
                        visited[nr][nc] = True
                        queue.append((nr,nc))
                        
        #문제 조건에 따른 결과 출력
        print(f"{tc} {len(queue)}")
         
                    
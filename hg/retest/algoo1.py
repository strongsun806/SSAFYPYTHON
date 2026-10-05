# 파리 퇴치 변형 
T = int(input())

for tc in range(1, T+1):
    N,M,K = map(int,input().split())
    grid = [list(map(int,input().split())) for _ in range(N)]
    
    count = 0 #조건을 만족하는 구역 수 
    
    # 1. M*M 파리채 좌상단 기준점 (r,c) 순회
    for r in range(N-M +1):
        for c in range(N-M+1):
            total = 0 
            for dr in range(M):
                for dc in range(M):
                    total += grid[r+dr][c+dc]
            
            # 3. K 이상인 경우 카운트 증가
            if total >= K:
                count += 1
                
    print(f"{tc} {count}")
    

    
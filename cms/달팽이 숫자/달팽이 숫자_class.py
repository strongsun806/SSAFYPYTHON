import sys
sys.stdin = open("input.txt","r")

# 테스트 케이스 갯수 T
T = int(input())
for tc in range (1,T+1):
    # 가로세로 칸 갯수 N
    N = int(input())
    # N 길이만큼 요소 0을 가진 2차원 배열 arr 생성
    arr = [[0]*N for _ in range(N)]
    num = 1
    r,c= 0,0   # 시작점은 좌측 상단
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    d = 0   # 현재 방향은 0으로 초기화
    # 숫자 넣고 다음칸 이동하는 것을 반복
    while num <=N**2:   # N**2보다 작거나 같으면 숫자넣기 반복
        arr[r][c] = num
        r += dirs[d][0]
        c += dirs[d][1]
        num += 1
        if r<0 or r>=N or c<0 or c>=N or arr[r][c] !=0 :
            r -= dirs[d][0]
            c -= dirs[d][1]
            d += (d+1)%4
            r += dirs[d][0]
            c += dirs[d][1]

    print(f"#{tc}")
    for i in range(N):
        for j in range(N):
            # 열 마다 공백으로 출력
            print(f"{arr[i][j]}", end=" ")
        # 행 마다 개행
        print()


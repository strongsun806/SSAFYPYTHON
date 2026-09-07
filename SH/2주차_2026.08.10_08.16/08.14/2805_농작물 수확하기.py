import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    # 농작물을 수확해 얻는 수익 초기값 세팅
    income = 0
    # 각 행과 열의 중심점 잡기
    center = N // 2

    for i in range(N):
        # 대칭인것을 이용해서 중심에서 부터 시작할 거리 계산
        distance = abs(i - center)
        # 중심에서 대칭점을 기준으로 열로 이동할 때, 계산할 시작과 끝 범위 설정
        for a in range(distance, N - distance):
            # 열로 이동할 때마다 농작물을 수확해 얻는 수익을 income 변수에 계속 더하기
            income += farm[i][a]
            
    print(f"#{test_case} {income}")


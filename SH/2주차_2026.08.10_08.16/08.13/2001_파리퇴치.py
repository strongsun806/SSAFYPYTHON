import sys
sys.stdin = open("input.txt", "r")

T = int(input()) 

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 파리채로 잡은 파리 중 가장 큰 값 초기 세팅
    max_sum = 0

    # 중첩 for문을 활용해 N x N 배열을 하나씩 도는 반복문 설정
    # 단, 파리채가 마지막 인덱스 전까지 가야하기 때문에 N - M + 1로 범위 설정
    for i in range(N - M + 1):
        for j in range(N - M + 1):

            # 파리채로 잡은 파리 개수 합 초기값 세팅
            sum_v = 0

            # 중첩 for문을 활용해 파리채가 잡는 인덱스 범위를 설정
            for a in range(i, i + M):
                for b in range(j, j + M):
                    # 범위안에 들어오는 값들을 sum_v값에 할당
                    sum_v += arr[a][b]

            # if문을 활용해 가장 큰 값을 max_v에 할당
            if sum_v > max_sum:
                max_sum = sum_v

    print(f"#{test_case} {max_sum}")
import sys

sys.stdin = open("D2_4835. [SW 문제해결 기본] 1일차 - 구간합/input.txt", "r")

T = int(input()) # 3
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 일단 input 받아버렷! 두 번 받아버렷!
    N, M = map(int, input().split())
    # print(N, M)
    list_1 = []
    list_1.extend(map(int, input().split()))

    # (숫자M개의 배열의 제일 왼쪽을 기준으로) 인덱스 0부터 N-M+1까지 순회하면서
    # list의 [j]부터 M개의 숫자를 더함 -> sum_nums_M에 누적합으로서 sum함수 대신했음.
    # 안쪽 for문이 끝났을때(즉, sum_nums_M의 값이 정해졌을 때)
    # 최댓값보다 크면 그 값을 최댓값으로 갱신하고
    # 최솟값보다 작으면 그 값을 최솟값으로 갱신하면,
    # 순회가 모두 끝났을 때 max_sum과 min_sum의 값으로 계산하면 결과가 나온다.
    max_sum = 0
    min_sum = float('inf')
    for i in range(0, N-M+1):
        sum_nums_M = 0
        for j in range(M):
            sum_nums_M += list_1[i+j] # i번째 인덱스값에서 0으로 시작하는 j부터 M개의 숫자를 더하는것이므로 i+j임
                                      # 처음에 틀림 ㅠ
        if sum_nums_M > max_sum:
            max_sum = sum_nums_M
        if sum_nums_M < min_sum:
            min_sum = sum_nums_M

    print(f'#{test_case} {max_sum-min_sum}')

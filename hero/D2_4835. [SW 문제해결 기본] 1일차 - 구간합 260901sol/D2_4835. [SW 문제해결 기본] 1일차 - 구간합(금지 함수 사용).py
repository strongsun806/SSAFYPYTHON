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

    # 숫자 계산 잘 봐야함
    # i 인덱스부터 M개를 다 더한거를 list_sum에 append하기
    list_sum = []
    for i in range(0, N-M+1):
        list_sum.append(sum(list_1[i:i+M]))

    # 바로 계산해서 출력 ㅋ
    print(f'#{test_case} {max(list_sum)-min(list_sum)}')

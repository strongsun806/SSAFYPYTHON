import sys

sys.stdin = open("D2_4828. [SW 문제해결 기본] 1일차 - min max/input.txt", "r")

T = int(input()) # 3

for test_case in range(1, T + 1):
    # 일단 input 받아버렷! 두 번 받아버렷!
    N = int(input())
    list_num = []
    list_num.extend(map(int, input().split()))

    # 문제에서 1이상 1000000이하라고 했으니 초기값 설정을 다음과 같이 함
    max_num = 0
    min_num = 1000000

    # 0부터 N까지 순회하면서 max와 min값을 조건에 맞게 최신화
    for i in range(N):
        if list_num[i] > max_num:
            max_num = list_num[i]
        if list_num[i] < min_num:
            min_num = list_num[i]

    print(f'#{test_case} {max_num - min_num}')
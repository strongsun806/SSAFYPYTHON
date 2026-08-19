# 다음과 같은 입력이 주어졌을 때, 이를 처리하는 코드를 작성하세요.

# [입력]
# 첫 줄에 두 개의 정수 N과 M이 주어집니다. N은 배열의 크기, M은 구간의 개수입니다.
# 두 번째 줄에 N개의 정수가 공백으로 구분되어 주어집니다.
# 그 다음 M개의 줄에 각각 두 개의 정수 i와 j가 주어집니다.

# 5 3
# 1 2 3 4 5
# 1 3
# 2 4
# 3 5

# [출력]
# 배열의 i번째 수부터 j번째 수까지의 합을 각 줄마다 출력하는 프로그램을 작성하세요. 
# (인덱스는 1부터 시작합니다)

# 6
# 9
# 12

import sys
sys.stdin = open("input.txt", "r")

# T = int(input())
# for test_case in range(1, T + 1):

list_1 = list(map(int, input().split()))
n = list_1[0]
m = list_1[1]
list_arr = list(map(int, input().split()))
for a in range(m):
    list_cnt = list(map(int, input().split()))
    i = list_cnt[0]
    j = list_cnt[1]
    list_subarr = list_arr[i-1:j]
    sum_subarr = 0
    for b in list_subarr:
        sum_subarr += b
    print(sum_subarr)
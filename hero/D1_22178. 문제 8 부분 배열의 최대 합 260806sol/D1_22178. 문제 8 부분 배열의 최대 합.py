# 다음과 같은 입력이 주어졌을 때, 이를 처리하는 코드를 작성하세요.

# ```
# 8 3
# 1 2 3 4 5 6 7 8
# ```

# 21

# 첫 줄에 두 개의 정수 N과 K가 주어집니다. N은 배열의 크기, K는 부분 배열의 크기입니다.
# 두 번째 줄에 N개의 정수가 공백으로 구분되어 주어집니다.
# 이 배열에서 연속된 K개의 원소로 이루어진 부분 배열 중
# 그 합이 최대인 것을 찾아 그 합을 출력하는 프로그램을 작성하세요.


import sys
sys.stdin = open("input.txt", "r")

list_1 = list(map(int, input().split()))
list_2 = list(map(int, input().split()))
max_of_sum = 0
arr_size = list_1[0]
subarr_size = list_1[1]
target_size = (arr_size) - (subarr_size - 1)
for i in range(target_size):
    if (list_2[i] + list_2[i+1] + list_2[i+2]) >= max_of_sum:
        max_of_sum = (list_2[i] + list_2[i+1] + list_2[i+2])
print(max_of_sum)
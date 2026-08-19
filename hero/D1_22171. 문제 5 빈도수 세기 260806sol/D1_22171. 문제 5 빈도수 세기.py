# 다음과 같은 입력이 주어졌을 때, 이를 처리하는 파이썬 코드를 작성하세요.
# ```
# 8
# 1 2 3 2 1 3 2 1
# ```
# 첫 줄은 숫자의 개수 N을 나타내고, 두 번째 줄은 N개의 정수가 공백으로 구분되어 주어집니다.
# 각 숫자의 등장 빈도수를 계산하여 출력하는 프로그램을 작성하세요.
# 출력은 숫자와 빈도수를 공백으로 구분하여 한 줄에 하나씩 출력하되, 숫자가 작은 순서대로 출력하세요.
# 1 3
# 2 3
# 3 2
import sys
sys.stdin = open("input.txt", "r")

# T = int(input())
# for test_case in range(1, T + 1):

n = int(input())
list_num = list(map(int, input().split()))
a = set()
count = 0
for i in range(n):
    a.add(list_num[i])
list_title_num = list(a)

for j in list_title_num:
    print(list_title_num[j-1], list_num.count(j))
import sys
sys.stdin = open("input.txt", "r")

T = int(input()) # 3
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 2 + 1):
    # N값 받기
    N = int(input())

    # 리스트에 받기
    list_numbers = list(map(int, input().split()))

    print(list_numbers)

    # 문제에서 요구하는 (j-i)(A[i]+A[j])의 max값은 사다리꼴의 넓이의 max값과 같다.
    # 따라서 시각적으로 생각해볼 필요가 있다.
    # 
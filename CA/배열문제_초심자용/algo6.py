import sys
sys.stdin = open("algo6_in.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    listed = list(map(int, input().split()))

    count_list = [0] * 101
    for i in range(N):
        count_list[listed[i]] += 1

    max_count = 0
    ans = 0
    for i in range(101):
        if count_list[i] > max_count:
            max_count = count_list[i]
            ans = i

    print(f"#{test_case} {ans}")

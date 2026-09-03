import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = tuple(map(int, input().split()))
    num_list = list(map(int, input().split()))

    sum_max = None
    sum_min = None
    for i in range(N-M+1):
        num = 0
        for j in range(0,M) :
            num += num_list[i+j]
        if i == 0 :
            sum_max = num
            sum_min = num
        elif num > sum_max:
            sum_max = num
        elif num < sum_min:
            sum_min = num

    print(f"#{test_case} {sum_max-sum_min}")
            

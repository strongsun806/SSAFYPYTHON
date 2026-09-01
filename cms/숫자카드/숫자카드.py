import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    counts = [0]*10
    N = int(input())
    nums = int(input())
    for i in range(N):
        counts[nums % 10] += 1
        nums //= 10
    h_num = 0
    h_count = counts[0]
    for j in range(1,10):
        if counts[j] >= h_count :
            h_num = j
            h_count = counts[j]

    print(f"#{test_case} {h_num} {h_count}")
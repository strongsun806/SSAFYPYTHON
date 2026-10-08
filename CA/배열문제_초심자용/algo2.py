import sys
sys.stdin = open("algo2_in.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    listed = list(map(int, input().split()))

    hap = 0
    for i in range(N):
        if i % 2 == 0:
            hap += listed[i]

    print(f"#{test_case} {hap}")

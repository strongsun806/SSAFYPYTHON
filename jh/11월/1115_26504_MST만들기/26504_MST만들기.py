import sys
sys.stdin = open('2_sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    c = sorted(map(int, input().split()))

    mn = sum(c[:n - 1])
    mx = sum(c[k * (k - 1) // 2] for k in range(1, n))
    print(mn, mx)
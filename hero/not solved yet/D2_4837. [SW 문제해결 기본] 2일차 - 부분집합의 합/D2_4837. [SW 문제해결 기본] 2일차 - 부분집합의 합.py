import sys
sys.stdin = open("D2_4837. [SW 문제해결 기본] 2일차 - 부분집합의 합/input.txt", "r")

T = int(input())  # 1이상 50이하

for test_case in range(1, T + 1):
    N, K = map(int, input().split())  # N은 1이상 12이하, K는 1이상 100이하
    A = []
    for i in range(1, 12 + 1):
        A.append(i)
    print(A)

    n = 0
    while n < N:

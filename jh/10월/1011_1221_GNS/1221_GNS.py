import sys
sys.stdin = open('GNS_test_input.txt', 'r')

T = int(input())
for _ in range(1, T+1):
    tc, N = input().split()
    N = int(N)
    nums = input().split()
    arr = [
        ["ZRO", 0],
        ["ONE", 0],
        ["TWO", 0],
        ["THR", 0],
        ["FOR", 0],
        ["FIV", 0],
        ["SIX", 0],
        ["SVN", 0],
        ["EGT", 0],
        ["NIN", 0],
           ]
    for i in nums:
        for j in range(len(arr)):
            if i == arr[j][0]:
                arr[j][1] += 1
                break
    print(tc)
    for num, cnt in arr:
        for _ in range(cnt):
            print(num, end=' ')
    print()




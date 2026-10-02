import sys
sys.stdin = open("GNS_test_input.txt","r")

GNS_num = ["ZRO", "ONE", "TWO", "THR", "FOR","FIV", "SIX", "SVN", "EGT", "NIN"]

T= int(input())
for tc in range(1,T+1):
    N, M = input().split()
    M = int(M)
    nums = input().split()
    count = [0]*10

    for num in nums :
        for i in range(10):
            if num == GNS_num[i]:
                count[i] += 1
                break

    result = []
    for i in range(10):
        for _ in range(count[i]):
            result.append(GNS_num[i])

    print(N)
    print(' '.join(result))
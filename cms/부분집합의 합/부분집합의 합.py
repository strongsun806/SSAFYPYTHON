import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
arr_A = list(range(1,13))
for tc in range(1,T+1):
    check = [0]*12
    cnt = 0
    N, K = map(int,input().split())
    for i in range(1<<12):
        cnt_s = 0
        sum_s = 0
        for j in range(12):
            if i & (1<<j):
                sum_s += arr_A[j]
                cnt_s += 1
        if cnt_s == N and sum_s == K :
            cnt += 1
    print(f"#{tc} {cnt}")
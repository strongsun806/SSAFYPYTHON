import sys
sys.stdin = open('sample_input.txt')

def products(cnt, cur_sum):
    global total_min
    
    if cnt == N:
        if total_min > cur_sum:
            total_min = cur_sum

    if total_min <= cur_sum:
        return
    for i in range(N):
        if check[i] == 0:
            cur_sum += arr[cnt][i]
            check[i] = 1
            products(cnt+1, cur_sum)
            check[i] = 0
            cur_sum -= arr[cnt][i]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    check = [0]*N
    total_min = 15000
    products(0, 0)
    print(f'#{tc} {total_min}')

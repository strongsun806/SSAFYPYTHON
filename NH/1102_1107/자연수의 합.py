T = int(input())
for tc in range(1,T+1):
    M= int(input())

    num = 0
    sum_v = 0
    while sum_v > M:
        num += 1
        sum_v += num

    print(f'#{tc} {num}')
T = int(input())

for tc in range(1, T+1):
    N = float(input())

    result = ''
    for _ in range(12):
        if N == 0:
            break
        N *= 2
        if N >= 1:
            result += '1'
            N -= 1
        else:
            result += '0'

    if N > 0:
        print(f'#{tc} overflow')
    else:
        print(f'#{tc} {result}')
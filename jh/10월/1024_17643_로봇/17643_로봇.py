import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    x, y = map(int, input().split())
    possible = True

    while x != 0 or y != 0:
        rx = x % 3
        ry = y % 3
        if (rx == 0 and ry == 0) or (rx != 0 and ry != 0):
            possible = False
            break
        if rx != 0:
            if rx == 1:
                x -= 1
            else:
                x += 1
        else:
            if ry == 1:
                y -= 1
            else:
                y += 1
        x //= 3
        y //= 3

    if possible:
        print(f'#{tc} yes')
    else:
        print(f'#{tc} no')

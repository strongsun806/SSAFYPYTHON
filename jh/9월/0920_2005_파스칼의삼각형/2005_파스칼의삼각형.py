import sys
sys.stdin  = open('input.txt', 'r')

def pascal(r, c):
    if c == 0 or c == r:
        return 1
    return pascal(r - 1, c - 1) + pascal(r - 1, c)

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}')
    N = int(input())
    for i in range(N):
        for j in range(i + 1):
            print(pascal(i, j), end=' ')
        print()

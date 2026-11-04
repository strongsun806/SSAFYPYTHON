import sys
sys.stdin = open('sample_input.txt', 'r')

def cnt_square(box):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if box[i][j] == '#':
                cnt += 1
    return cnt

def f(box):
    global r, c
    for i in range(N):
        for j in range(N):
            if box[i][j] == '#':
                r, c = i, j
                return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    box = [list(input().strip()) for _ in range(N)]
    r = 0
    c = 0
    a = 0
    is_square = 'yes'
    cnt_s = cnt_square(box)
    f(box)
    while 0<=c+a<N and box[r][c+a] == '#':
        a += 1
    for i in range(a):
            for j in range(a):
                if box[r+i][c+j] == '.':
                    is_square = 'no'
    if cnt_s != a**2:
        is_square = 'no'
    
    print(f'#{tc} {is_square}')
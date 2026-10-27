import sys
sys.stdin = open('input.txt')

def find_start():
    global r, c
    for i in range(H):
        for j in range(W):
            if map_t[i][j] == '^':
                r = i
                c = j
                return
            if map_t[i][j] == 'v':
                r = i
                c = j
                return
            if map_t[i][j] == '<':
                r = i
                c = j
                return
            if map_t[i][j] == '>':
                r = i
                c = j
                return

def operation_U(r, c):
    map_t[r][c] = '^'
    if 0<= r-1 < H and map_t[r-1][c] == '.':
        map_t[r][c] = '.'
        map_t[r-1][c] = '^'
        return r-1, c
    return r, c

def operation_D(r, c):
    map_t[r][c] = 'v'
    if 0<= r+1 < H and map_t[r+1][c] == '.':
        map_t[r][c] = '.'
        map_t[r+1][c] = 'v'
        return r+1, c
    return r, c

def operation_L(r, c):
    map_t[r][c] = '<'
    if 0<= c-1 < W and map_t[r][c-1] == '.':
        map_t[r][c] = '.'
        map_t[r][c-1] = '<'
        return r, c-1
    return r, c

def operation_R(r, c):
    map_t[r][c] = '>'
    if 0<= c+1 < W and map_t[r][c+1] == '.':
        map_t[r][c] = '.'
        map_t[r][c+1] = '>'
        return r, c+1
    return r, c

def shoot(r, c):
    a = 0
    if map_t[r][c] == '^':
        while True:
            a += 1
            if 0 <= r-a < H and map_t[r-a][c] == '*':
                map_t[r-a][c] = '.'
                return
            if not 0 <= r-a < H or map_t[r-a][c] == '#':
                return
            
    if map_t[r][c] == 'v':
        while True:
            a += 1
            if 0 <= r+a < H and map_t[r+a][c] == '*':
                map_t[r+a][c] = '.'
                return
            if not 0 <= r+a < H or map_t[r+a][c] == '#':
                return
            
    if map_t[r][c] == '<':
        while True:
            a += 1
            if 0 <= c-a < W and map_t[r][c-a] == '*':
                map_t[r][c-a] = '.'
                return
            if not 0 <= c-a < W or map_t[r][c-a] == '#':
                return
            
    if map_t[r][c] == '>':
        while True:
            a += 1
            if 0 <= c+a < W and map_t[r][c+a] == '*':
                map_t[r][c+a] = '.'
                return
            if not 0 <= c+a < W or map_t[r][c+a] == '#':
                return


T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    map_t = [list(input().strip()) for _ in range(H)]
    N = int(input().strip())
    op = list(input().strip())
    r, c = 0, 0
    find_start()
    for oper in op:
        if oper == 'U':
            r, c = operation_U(r, c)
        elif oper == 'D':
            r, c = operation_D(r, c)
        elif oper == 'L':
            r, c = operation_L(r, c)
        elif oper == 'R':
            r, c = operation_R(r, c)
        elif oper == 'S':
            shoot(r, c)

    print(f'#{tc}', end=' ')
    for i in range(H):
        for j in range(W):
            print(map_t[i][j], end='')
        print()

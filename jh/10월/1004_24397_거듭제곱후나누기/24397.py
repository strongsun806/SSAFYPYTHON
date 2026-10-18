import sys
sys.stdin = open('2_sample_input.txt', 'r')

T = int(input ())
for tc in range(1, T+1):
    x, y, z =  map(int, input().split())
    tmp_x = x%(1000*z)
    tmp_x1 = x%(1000*z)
    tmp_y = [y]

    check = 1
    is_large = False
    if x >= 2:
        for _ in range(y):
            check *= x
            if check >= 1000 * z:
                is_large = True
                break

    while y != 1:
        if y % 2:
            y = (y-1) // 2
            tmp_y.append(y)
        else:
            y = y // 2
            tmp_y.append(y)
    tmp_y.pop()
    tmp_y = tmp_y[::-1]

    for yi in tmp_y:
        if yi % 2:
            tmp_x **= 2
            tmp_x *= tmp_x1
            tmp_x = tmp_x%(1000*z)
        else:
            tmp_x **= 2
            tmp_x = tmp_x%(1000*z)

    ans_int = tmp_x // z
    ans_float = (tmp_x % z) * 1000 // z

    ans_int = str(ans_int)
    ans_float = str(ans_float)

    if is_large:
        while len(ans_int) < 3:
            ans_int = '0' + ans_int
    while len(ans_float) < 3:
        ans_float = '0' + ans_float


    print(f'{ans_int}.{ans_float}')


    
        
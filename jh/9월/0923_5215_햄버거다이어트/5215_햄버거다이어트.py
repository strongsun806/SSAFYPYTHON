import sys, time
sys.stdin = open('sample_input.txt', 'r')

# start = time.time()

# 버거조합
def choose(start):
    # print('start', start)
    global car, max_taste

    if car > L:
        # print('2', stack)
        tmp_stack = stack[:]
        tmp_stack.pop()
        taste = sum(tmp_stack)
        if max_taste < taste:
            max_taste = taste
        return

    if start == N:
        # print('3', stack)
        taste = sum(stack)
        if max_taste < taste:
            max_taste = taste
        return

    for i in range(start, N):
        car += burgers[i][1]
        stack.append(burgers[i][0])
        # print('1', stack)
        choose(i+1)
        car -= burgers[i][1]
        stack.pop()


T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    burgers = [list(map(int, input().split())) for _ in range(N)]
    stack = []
    car = 0
    max_taste = 0
    choose(0)
    print(f'#{tc} {max_taste}')

# end = time.time()

# print(f'{end- start:.4f}초')
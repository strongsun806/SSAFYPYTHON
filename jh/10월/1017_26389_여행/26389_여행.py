import sys
sys.stdin = open('1_sample_input.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    data = list(input().strip())
    if len(data) == 1:
        print('No')
        continue
    data = list(set(data))
    ns = 0
    we = 0
    for d in data:
        if d == 'N':
            ns += 1
        elif d == 'S':
            ns -= 1
        elif d == 'W':
            we += 1
        elif d == 'E':
            we -= 1
    if ns == 0 and we == 0:
        print('Yes')
    else:
        print('No')



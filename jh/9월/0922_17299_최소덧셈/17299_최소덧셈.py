import sys
sys.stdin = open('sample_input.txt','r')
T = int(input())
for tc in range(1, T+1):
    min_v = 99999999
    num = input()
    for i in range(1, len(num)):
        a = ''
        b = ''
        a += num[0:i]
        b += num[i:len(num)]
        c = int(a)+int(b)
        if min_v > c:
            min_v = c
    print(f'#{tc} {min_v}')

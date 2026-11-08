import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    ans = ''
    N, num16 = input().split()
    print(num16)
    num10 = int(num16, 16)
    print(num10)
    ans = format(num10, f'0{int(N) * 4}b')
    print(f'#{tc} {ans}')

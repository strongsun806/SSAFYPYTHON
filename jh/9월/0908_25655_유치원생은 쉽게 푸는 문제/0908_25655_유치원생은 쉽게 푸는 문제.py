import sys
sys.stdin = open('1_sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    X = int(input())
    a = X // 2
    b = X % 2
    final = '4'*b+'8'*a
    if a == 0 and b == 1:
        final = 0
    print(final)
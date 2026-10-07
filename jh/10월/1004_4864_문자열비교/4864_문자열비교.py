import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    str1 = input().strip()
    str2 = input().strip()
    N1 = len(str1)
    N2 = len(str2)
    is_cor = False
    for i in range(N2-N1+1):
        tmp_str = str2[i:i + N1]
        if str1 == tmp_str:
            is_cor = True
            break
    if is_cor:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
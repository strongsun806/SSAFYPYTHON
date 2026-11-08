import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    sen = list(input().strip())
    chars = list(set(sen))
    N = len(chars)
    cnt_char = [0]*N
    is_ok  = True
    for i in range(N):
        for char in sen:
            if chars[i] == char:
                cnt_char[i] += 1
    for cnt in cnt_char:
        if cnt != 2:
            is_ok = False
    
    if is_ok:
        print(f'#{tc} Yes')
    else:
        print(f'#{tc} No')
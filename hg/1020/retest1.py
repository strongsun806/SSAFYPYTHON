T = int(input())
for tc in range(1, T+1):
    N, hex = input().split()
    ans = ''
    for ch in hex:
        ans += format(int(ch, 16), '04b')
        
    print(f'#{tc} {ans}')
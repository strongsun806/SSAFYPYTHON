# 이거 문제 되게 짧게 푼 사람 있길래 베껴옴
T = int(input())

for tc in range(1, T+1):
    N, hex = input().split()
    ans = ''
    for ch in hex:
        ans += format(int(ch, 16), '04b')
        
    print(f'#{tc} {ans}')
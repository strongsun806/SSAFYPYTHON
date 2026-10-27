T = int(input())

for tc in range(1, T + 1):
    N, hex_str = input().split()
    ans = ''
    
    # 1. 16진수를 2진수 문자열로 변환 (기존 코드)
    for ch in hex_str:
        ans += format(int(ch, 16), '04b')

    # 2. cnt = 0 설정 후 1의 개수 세기
    cnt = 0
    for bit in ans:
        if bit == '1':
            cnt += 1

    print(f'#{tc} {cnt}')
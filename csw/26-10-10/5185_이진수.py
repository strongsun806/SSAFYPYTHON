T = int(input())

for tc in range(1, T+1):
    N, hex_num = input().split()

    result = ''
    for ch in hex_num:
        dec_num = int(ch, 16)   # 입력받은건 문자.. 이제 숫자로 바꿀게
        bits = ''
        for _ in range(4):  # 바꾼 16진수를 이진수로 표현하는 과정.. 16진수는 2진수 4자리로 표현 가능
            bits = str(dec_num % 2) + bits
            dec_num //= 2
        result += bits

    print(f'#{tc} {result}')
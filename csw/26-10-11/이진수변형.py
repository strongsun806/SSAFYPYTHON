'''
N자리 16진수를 8진수로 출력하시오. 앞자리 0은 붙이지 않는다.

입력
1
4 47FE

출력
#1 43776
'''

T = int(input())

for tc in range(1, T+1):
    N, hex_num = input().split()

    result = ''
    for ch in hex_num:
        num = int(ch, 16)
        
        bits = ''
        for _ in range(4):
            bits = str(num % 2) + bits
            num //= 2
        result += bits

    # 16진수를 2진수로 바꿨는데 16진수는 한자리가 4비트
    # 8진수는 3비트 단위라서 자리수가 안맞음..
    # 그래서 padding해서 0을 채워줄거임
    # len(result) % 3 >> 3으로 묶고 남은 개수
    # 3 - len(result) % 3 >> 모자란 개수
    # (3 - len(result) % 3) % 3 >> 길이가 이미 3비트 단위일떄를 처리하기 위해 나눗셈의 나머지를 모자란 숫자의 개수로 보기
    pad = (3 - len(result) % 3) % 3
    result = '0' * pad + result

    oct_num = ''
    for i in range(0, len(result), 3):
        # int(result[i:i+3], 2) >> 패딩해준 result를 3개씩 끊어서 2진수로 전환
        # str(int(result[i:i+3], 2)) >> 다시 str로 바꾸기
        oct_num += str(int(result[i:i+3], 2))
    # int(oct_num) >> 앞자리 0은 붙이지 않는다. 조건때문에 해줌
    print(f'#{tc} {int(oct_num)}')
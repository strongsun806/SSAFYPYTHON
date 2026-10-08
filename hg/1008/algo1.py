HEX_TO_BIN = {
    '0' : '0000', '1' : '0001', '2' : '0010',
    '3' : '0011', '4' : '0100', '5' : '0101',
    '6' : '0110', '7' : '0111', '8' : '1000',
    '9' : '1001', 'A' : '1010', 'B' : '1011',
    'C' : '1100', 'D' : '1101', 'E' : '1110',
    'F' : '1111',
}

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    hex_str = input().strip()
    
    # 2진수 비트열 생성
    bin_str = ""
    for ch in hex_str:
        bin_str += HEX_TO_BIN[ch]
        
    #연속된 1의 최대 길이 측정
    max_len = 0
    current_len = 0
    for bit in bin_str:
        if bit == '1':
            current_len += 1
            if current_len > max_len:
                max_len = current_len
            else :
                current_len = 0
    print(f"#{tc} {max_len}")
# 16진수 한 글자를 4자리 2진수로 바꿔주는 함수 정의
def hex_to_bin_4bit(hex_char):
    # 16진수 문자를 10진수로 변환
    num = int(hex_char, 16)
    
    # 10진수를 2진수로 바꾸고 4자리 맞추기 (0000~1111)
    bin_str = format(num, '04b')
    return bin_str

# 메인 로직 (테스트케이스)
T = int(input())
for tc in range(1, T + 1):
    hex_input = input().strip()
    
    full_binary = ""
    for ch in hex_input:
        # 만든 함수를 가져와서 사용!
        full_binary += hex_to_bin_4bit(ch)
        
    print(f"#{tc} {full_binary}")
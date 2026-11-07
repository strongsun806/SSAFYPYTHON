# 2진수 3자리마다 대응하는 8진수 사전
b_to_o = {
    '000': '0', '001': '1', '010': '2', '011': '3',
    '100': '4', '101': '5', '110': '6', '111': '7'
}

T = int(input())
for test_case in range(1, T + 1):
    N, bin_str = input().split() # N은 자릿수, bin_str은 2진수 문자열
    
    # 1. 길이가 3의 배수가 아니면 앞에 '0'을 채워주기 (3자리씩 끊어야 하므로!)
    while len(bin_str) % 3 != 0:
        bin_str = '0' + bin_str
        
    ans = ""
    # 2. 3칸씩 건너뛰면서 3글자씩 잘라내고 8진수로 바꿔 이어붙이기
    for i in range(0, len(bin_str), 3):
        chunk = bin_str[i:i+3] # 3글자씩 뚝뚝 끊기
        ans += b_to_o[chunk]   # 딕셔너리에서 찾아서 붙이기
        
    print(f"#{test_case} {ans}")
#이진수를 쉽게 푸는 방법은
#파이썬 내장함수를 사용하거나 비트연산/딕셔너리
#근데 파이썬 내장함수 외우는 게 좀 더 편하겠죠?

# 이건 16진수 1자리를 2진수 4자리로 바꾸는 거다
T = int(input())

for tc in range(1, T+1):
    N, hex_str = input().split() #N이랑 16진수를 인풋받아옴
    ans = ""  # 정답을 담을 곳을 일단 빈칸으로 넣어둠
    
    for char in hex_str:
        num = int(char,16)
        ans += format(num, '04b')
        
    print(f"#{tc} {ans}")

'''
(function) def format(
 value: object,
 format_spec: str = "",
 /
) -> str

Return value.__format__(format_spec)

format_spec defaults to the empty string. 

See the Format Specification Mini-Language section of help('FORMATTING') for details.
'''


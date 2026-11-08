#이번엔 반대로 2진수를 16진수로 바꿔와보겠음

T = int(input())

for tc in range(1, T+1):
    N, bin_str = input().split()
    ans = ""
    for i in range(1, int(N), 4):
        chunk = bin_str[i:i+4]
        val = int(chunk, 2)
        ans += format(val, 'X')
        
    print(f"#{tc} {ans}")
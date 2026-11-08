# Professional - 조합
# import sys

# sys.stdin = open("sample_input.txt", "r")

MOD = 1234567891
MAX = 1000000

# 1. 팩토리얼 미리 전처리 (1! ~ 1,000,000!)
fact = [1] * (MAX + 1)
for i in range(1, MAX + 1):
    fact[i] = (fact[i - 1] * i) % MOD

# 거듭제곱 분할 정복 (또는 파이썬 내장 pow(base, exp, MOD) 사용 가능)
def power(base, exp):
    res = 1
    base %= MOD
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % MOD
        base = (base * base) % MOD
        exp //= 2
    return res

T = int(input())

for tc in range(1, T + 1):
    N, R = map(int, input().split())

    # 분자: N!
    numerator = fact[N]
    
    # 분모: R! * (N - R)!
    denominator = (fact[R] * fact[N - R]) % MOD

    # 페르마의 소정리: denominator^(MOD - 2) % MOD
    # power(denominator, MOD - 2) 대신 파이썬 내장 pow(denominator, MOD - 2, MOD) 사용 가능
    inv_denominator = power(denominator, MOD - 2)

    ans = (numerator * inv_denominator) % MOD
    print(f"#{tc} {ans}")
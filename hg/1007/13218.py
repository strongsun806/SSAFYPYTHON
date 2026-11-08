# N명의 수강생을 3명으로 나누면 될 거 같은데용

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ans = N // 3
    print(f"#{tc} {ans}")


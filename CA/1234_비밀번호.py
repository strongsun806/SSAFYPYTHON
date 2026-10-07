# ========================================================
# 문제: 1234_[S/W 문제해결 기본] 10일차 - 비밀번호
# 난이도: D3
# 작성자: 윤형섭 (1627575)
# 제출 결과: Pass
# 저장 일시: 2026-10-07 11:38:22
# ========================================================

#import sys
#sys.stdin = open("input10.txt","r")
T = 10
 for tc in range(1, T + 1):
    N_str, numbers = input().split()
    N = int(N_str)
         stack = [0] * N
    top = -1
         i = 0
    while i < len(numbers):
        char = numbers[i]
                 if top >= 0 and stack[top] == char:
            top -= 1
        else:
            top += 1
            stack[top] = char
                     i += 1
             result = "".join(stack[:top + 1])
    print(f"#{tc} {result}")

# ========================================================
# 문제: 1222_[S/W 문제해결 기본] 6일차 - 계산기1
# 난이도: D4
# 작성자: 윤형섭 (1627575)
# 제출 결과: Pass
# 저장 일시: 2026-10-07 11:34:11
# ========================================================

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    exp = input()
         # 후위 표기법 변환을 위한 스택
    postfix = []
    stack = []
         for char in exp:
        if char.isdigit():
            postfix.append(char)
        elif char == '+':
            while stack:
                postfix.append(stack.pop())
            stack.append(char)
                 while stack:
        postfix.append(stack.pop())
             # 후위 표기식 계산
    calc_stack = []
    for token in postfix:
        if token.isdigit():
            calc_stack.append(int(token))
        elif token == '+':
            num2 = calc_stack.pop()
            num1 = calc_stack.pop()
            calc_stack.append(num1 + num2)
                 print(f"#{test_case} {calc_stack[0]}")

import sys
# sys.stdin = open("input.txt", "r")

# 연산자 우선순위 정의
icp = {'+': 1, '*': 2}
isp = {'+': 1, '*': 2}

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    exp = input()
    
    # 1. 후위 표기법으로 변환
    postfix = []
    stack = []
    
    for char in exp:
        if char.isdigit():
            postfix.append(char)
        else:
            while stack and isp[stack[-1]] >= icp[char]:
                postfix.append(stack.pop())
            stack.append(char)
            
    while stack:
        postfix.append(stack.pop())
        
    # 2. 후위 표기식 계산
    calc_stack = []
    for token in postfix:
        if token.isdigit():
            calc_stack.append(int(token))
        else:
            num2 = calc_stack.pop()
            num1 = calc_stack.pop()
            if token == '+':
                calc_stack.append(num1 + num2)
            elif token == '*':
                calc_stack.append(num1 * num2)
                
    print(f"#{test_case} {calc_stack[0]}")

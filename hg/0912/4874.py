T = int(input())

for tc in range(1, T + 1):
    tokens = input().split()
    stack = []
    error = False

    for token in tokens:
        if token == '.':
            # 종료 시점에 스택에 결과값 하나만 남아 있어야 정상
            if len(stack) != 1:
                error = True
            break

        if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
            stack.append(int(token))
        elif token in ('+', '-', '*', '/'):
            # 연산자 처리: 피연산자가 최소 2개 필요
            if len(stack) < 2:
                error = True
                break
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b)
        else:
            # 유효하지 않은 토큰인 경우
            error = True
            break

    if error:
        print(f"#{tc} error")
    else:
        print(f"#{tc} {stack[0]}")
import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    N = int(input())
    nums = input().strip()

    # 후위표기식을 저장하는 배열
    fx = [-1] * N
    fx_top = -1

    # 연산자를 저장하는 스택
    stack = [None] * N
    top = -1

    # 중위표기식 → 후위표기식
    for x in nums:
        if x.isdigit():
            fx_top += 1
            fx[fx_top] = int(x)

        elif x == "+":
            # 기존 + 연산자가 있으면 먼저 출력
            while top >= 0:
                fx_top += 1
                fx[fx_top] = stack[top]
                top -= 1

            # 현재 + 연산자를 스택에 저장
            top += 1
            stack[top] = x

    # 남은 연산자를 후위표기식에 추가
    while top >= 0:
        fx_top += 1
        fx[fx_top] = stack[top]
        top -= 1

    # 후위표기식 계산
    stack = [0] * N
    top = -1

    for i in range(fx_top + 1):
        if fx[i] == "+":
            # 오른쪽 숫자 꺼내기
            right = stack[top]
            top -= 1

            # 왼쪽 숫자 꺼내기
            left = stack[top]
            top -= 1

            # 계산 결과를 다시 스택에 넣기
            top += 1
            stack[top] = left + right

        else:
            # 숫자를 스택에 넣기
            top += 1
            stack[top] = fx[i]

    print(f"#{tc} {stack[top]}")
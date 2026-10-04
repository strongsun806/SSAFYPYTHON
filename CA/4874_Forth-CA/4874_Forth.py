import sys
sys.stdin = open("input.txt", "r")

t = int(input())
for tc in range(1, t + 1):
    line = input().split()
    stack_num = []
    i = 0
    pointer = 0
    is_error = False

    while line[i] != '.':
        if line[i] in '+-*/':
            # 연산하려면 앞에 숫자가 2개(포인터 위치 2 이상) 필요
            if pointer < 2:
                is_error = True
                break

            if line[i] == '+':
                stack_num[pointer - 2] = stack_num[pointer - 2] + stack_num[pointer - 1]
            elif line[i] == '-':
                stack_num[pointer - 2] = stack_num[pointer - 2] - stack_num[pointer - 1]
            elif line[i] == '*':
                stack_num[pointer - 2] = stack_num[pointer - 2] * stack_num[pointer - 1]
            elif line[i] == '/':
                stack_num[pointer - 2] = stack_num[pointer - 2] // stack_num[pointer - 1]

            # 2개를 합쳐 1개가 되었으므로 포인터는 1만 줄고, 맨 뒤 1개만 pop
            pointer -= 1
            stack_num.pop()

        else:
            # 숫자는 리스트에 새로 추가하면서 포인터 증가
            stack_num.append(int(line[i]))
            pointer += 1

        i += 1

    # 연산 완료 후 숫자가 정확히 1개(pointer == 1) 남아있어야 정상
    if is_error or pointer != 1:
        print(f"#{tc} error")
    else:
        print(f"#{tc} {stack_num[0]}")
import sys
sys.stdin = open("input.txt", "r")
from collections import deque

T = int(input())  # 테스트 케이스 input 받기

for test_case in range(1, T + 1):
    # 앞에서부터 하나씩 빼서 확인할거라 popleft()를 쓸 수 있는 deque로 받기
    list_cal = deque(map(str, input().split()))

    # print(list_cal)

    # input을 str로 받았으니 숫자인 것들을 찾아서 int로 바꿔주기
    # 연산자는 '+', '-', '*', '/' 같은 연산자들이 str type 그대로 남아있음
    for i in range(len(list_cal)):
        if list_cal[i].isdecimal() == 1:
            list_cal[i] = int(list_cal[i])


    # 맨 앞에 있는 연산자를 찾고, 그 연산자 기준으로 앞에 2개를 이용해서 계산한 값을 그 자리에 두는 방식으로
    # 최종값이 나오거나, ERROR가 뜰 때까지 반복
    # 맨 앞에 있는 연산자는 stack에 쌓다가 str이 나오면 판단하는 식으로 하면 될 듯
    # 숫자들을 쌓아둘 stack
    stack_cal = []

    # 계산식은 무조건 '.'으로 끝나야하니까 맨 뒤를 빼면서 확인
    # 여기서 '.'을 미리 빼버리므로 아래 while문에서는 숫자와 연산자만 확인하면 됨
    
    try:
        if list_cal.pop() == '.':
            # list_cal에 처리할 숫자나 연산자가 남아있는 동안 계속 반복
            while len(list_cal):  #
                # int라면 숫자니까 계산하지 않고 일단 stack에 쌓기
                if type(list_cal[0]) == int:
                    stack_cal.append(list_cal.popleft())

                elif type(list_cal[0]) == str:  # 또는 else
                                                # "만약 연산자라면"
                    # 연산자가 나오면 stack에 가장 최근에 들어온 숫자 2개를 꺼내서 계산해야함
                    end = stack_cal.pop()       # end에 해당하는게 뒤에 있으므로 먼저 꺼내야함 ㅇㅇ
                    front = stack_cal.pop()

                    # 현재 확인하고 있는 연산자를 list_cal에서 꺼내서 따로 저장
                    # 아래에서 연산자 종류에 따라서 각각 계산해줄거임
                    operator = list_cal.popleft()

                    # front와 end 사이에 들어갈 연산자가 뭔지 확인해서 계산
                    # 계산한 결과는 다시 stack에 넣어줘야 이후 연산에 계속 사용할 수 있음
                    if operator == '+':
                        stack_cal.append(front + end)

                    elif operator == '-':
                        stack_cal.append(front - end)

                    elif operator == '*':
                        stack_cal.append(front * end)

                    elif operator == '/':
                        # 일반 나눗셈이라 결과가 float가 될 수 있음 -> int()
                        stack_cal.append(front / end)

                    elif operator == '//':
                        # 나눈 몫만 구하는 연산
                        stack_cal.append(front // end)

                    elif operator == '%':
                        # 나눈 나머지를 구하는 연산
                        stack_cal.append(front % end)

                    elif operator == '**':
                        # 제곱 연산
                        # ex) 2 ** 3 = 8
                        stack_cal.append(front ** end)
                    else:
                        # 위에서 처리하지 않은 연산자가 들어오면 잘못된 계산식으로 판단
                        raise Exception  # -> raise: 일부러 에러를 발생시키는 문법
                        # print(f'#{test_case} error')
                        # -> # 여기서 바로 print(f'#{test_case} error')를 해버리면 while문이 끝나는게 아니라 계속 진행됨
                             # 그리고 마지막의 len(stack_cal) 검사에서도 error가 또 출력될 수 있어서 중복 출력이 생길 수 있음
                             # 따라서 여기서는 일부러 에러를 발생시켜서 except로 바로 보내는게 깔끔함
                         
            # 모든 계산이 정상적으로 끝났다면 stack에는 최종 계산값 딱 1개만 남아있어야함
            if len(stack_cal) == 1:
                print(f'#{test_case} {stack_cal[0]}')

            else:  # 예외 및 에러 사항 1. 연산자는 다 썼는데, 숫자가 2개 이상 남은 경우
                print(f'#{test_case} error')
        else:  # 예외 및 에러 사항 2. 맨 뒤가 '.' 이 아닌 경우
            print(f'#{test_case} error')
                
    except Exception:  # 예외 및 에러 사항 3. 숫자가 부족하거나, 처리할 수 없는 연산자가 들어와서 오류가 생기는 경우
        # 숫자가 부족하면 pop() 과정에서 오류가 발생하고,
        # 처리하지 않는 연산자가 들어오면 위에서 raise Exception을 발생시켜서 여기로 옴
        print(f'#{test_case} error')



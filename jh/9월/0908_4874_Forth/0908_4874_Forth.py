import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = list(input().split())
    stack = []
    for i in range(len(arr)):
        # 숫자 인지 확인
        if arr[i] not in '*-+/.':
            arr[i] = int(arr[i])
        # 숫자면 스택에 추가 아니면 연산
        if type(arr[i]) == int:
            stack.append(arr[i])
        # .이나오면 값 출력 후 종료
        elif arr[i] == '.':
            if len(stack) ==1:
                num = stack.pop()
                print(f'#{tc} {int(num)}')
            else:
                print(f'#{tc} error')
        # 숫자도 아니고 . 도아님 : 연산
        else:
            # 스택의 길이가 2이상 일때만 연산 가능
            if len(stack) >= 2:
                a1 = stack.pop()
                b1 = stack.pop()
                if arr[i] == '*':
                    stack.append(b1*a1)
                elif arr[i] == '/':
                    if a1 == 0:
                        print(f'#{tc} error')
                        break
                    else:
                        stack.append(b1//a1)
                elif arr[i] == '+':
                    stack.append(b1+a1)
                elif arr[i] == '-':
                    stack.append(b1-a1)
            # 연산이 불가능 할때 error 출력
            else:
                print(f'#{tc} error')
                break


import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    N = int(input())
    nums = input().strip()
    func ={'+':0,'*':1}
    # 후위표기식을 저장하는 배열
    fx = [0] * N
    fx_top = -1

    # 연산자를 저장하는 스택
    stack = [0] * N
    top = -1

    # 중위표기식 → 후위표기식
    for x in nums:
        if x not in "+*":
            fx_top += 1
            fx[fx_top] = x

        else :
            if top == -1 or func[x]>func[stack[top]]:
                top+=1
                stack[top] = x
            else:
                while top > -1 and func[stack[top]]>=func[x]:
                    top -=1
                    fx_top +=1
                    fx[fx_top] = stack[top+1]
                top+=1
                stack[top]=x

    # 남은 연산자를 후위표기식에 추가
    while top >= 0:
        fx_top += 1
        fx[fx_top] = stack[top]
        top -= 1

    # 후위표기식 계산
    stack = [0] * N
    top = -1

    for i in range(fx_top+1):
        if fx[i] not in "+*":
            top +=1
            stack[top]=int(fx[i])

        else:
            top-=1
            op2=stack[top+1]
            top-=1
            op1=stack[top+1]

            if fx[i]=='+':
                top+=1
                stack[top]=op1+op2
            else:
                top+=1
                stack[top]=op1*op2

    print(f"#{tc} {stack[top]}")
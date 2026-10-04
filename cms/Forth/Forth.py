import sys
sys.stdin = open("sample_input.txt","r")

T = int(input())
for tc in range(1, T+1):
    data=list(input().split())
    stack = [0]*len(data)
    top = -1
    for i in range(len(data)):
        if data[i] in '+,-,/,*':
            if top<1 :
                print(f"#{tc} error")
                break
            else :
                top -=1
                if data[i] == '+':
                    stack[top] += stack[top+1]
                elif data[i] =='-':
                    stack[top] -= stack[top+1]
                elif data[i] =='/':
                    stack[top] //= stack[top+1]
                elif data[i] =='*':
                    stack[top] *= stack[top+1]
        elif data[i]== '.':
            if top == 0:
                print(f"#{tc} {stack[0]}")
            else : 
                print(f"#{tc} error")
                break
        else :
            top += 1
            stack[top] = int(data[i])

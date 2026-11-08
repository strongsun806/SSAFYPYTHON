import sys
sys.stdin = open("input.txt","r")

for tc in range(1,11):
    lenght= int(input())
    data = input()
    stack =[0]*lenght
    top = -1
    pair={')':'(','}':'{',']':'[','>':'<'}
    ans = 1
    for x in data:
        if x in'({[<':
            top += 1
            stack[top] = x
        elif x in')}]>':
            if top == -1 :
                ans = 0
                break
            else : 
                top -=1
                tmp = stack[top+1]
                if pair[x] != tmp:
                    ans = 0
                    break 

    if top != -1:   # 여는 괄호가 더 많은 경우
        ans = 0

    print(f"#{tc} {ans}")
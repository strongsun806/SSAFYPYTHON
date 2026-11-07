'''
(6+5*(2-8)/2)
6528-*2/+
'''

icp={'(':3,'*':2,'/':2,'+':1,'-':1}
isp={'(':0,'*':2,'/':2,'+':1,'-':1}
stack=[0]*100
top=-1

fx = '(6+5*(2-8)/2)'
susik =''   # 후위 연산식 기록할 빈 문자열

for  x in fx:
    if x not in '(+-*/)':
        susik += x
    elif x==')':   # 여는 괄호까지 pop
        while stack[top]!= '(':   #peek
            top -= 1
            susik += stack[top+1]
        top-= 1
    else :   #연산자인 경우
        if top == -1 or icp[x]>isp[stack[top]] :   # icp > top원소 isp : push
            top += 1
            stack[top] = x
        else:   # icp<= isp : isp>isp까지 pop
            while top > -1 and isp[stack[top]] >= icp[x]:
                top -=1
                susik += stack [top+1]
            top += 1   # push x
            stack[top] = x

print(susik)

for x in susik:
    if x not in '+-*/':   # 피연산자면 push
        top += 1
        stack[top]= int(x)
    else :   #연산자면
        # 피연산자 두 개를 꺼내서
        top -= 1
        op2 = stack[top+1]
        top -= 1
        op1 = stack[top+1]
        if x == '+':   # 연산 결과를 push
            top += 1
            stack [top] = op1 + op2
        elif x=='-':
            top += 1
            stack [top] = op1 - op2
        elif x=='/':
            top += 1
            stack [top] = op1 / op2
        elif x=='*':
            top += 1
            stack [top] = op1 * op2
top -=1
ans = stack[top+1]            
print(ans)

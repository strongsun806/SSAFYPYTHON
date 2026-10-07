import sys
sys.stdin = open("input11.txt","r")

t=10

for tc in range(1,t+1):
    N=int(input())
    stack=[]
    listed=input()
    braket=["{","[","(","<"]
    counter=-1
    i=0
    is_valid = 1
    while i<=N-1:
        if listed[i] in braket:
            stack.append(listed[i])
            i+=1
            counter+=1
        elif listed[i] not in "{}[]()<>":
            i+=1
        elif stack and listed[i] == "}" and stack[counter]=="{":
            stack.pop()
            counter-=1
            i+=1
        elif stack and listed[i] == "]" and stack[counter]=="[":
            stack.pop()
            counter-=1
            i+=1
        
        elif stack and listed[i] == ")" and stack[counter]=="(":
            stack.pop()
            counter-=1
            i+=1
        
        elif stack and listed[i] == ">" and stack[counter]=="<":
            stack.pop()
            counter-=1
            i+=1
        else:
            is_valid=0
            break
    if stack:
        is_valid=0
    print(f'#{tc}',is_valid)
        
        

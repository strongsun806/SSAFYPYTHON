s = []
def my_push(item):
    s.append(item)

def my_push(item,size):
    global top
    top +=1
    if top == size:
        print('OverFlow!')
    else:
        stack[top]=item

# 초기값
size=10
stack =[0]*size
top = -1

# push(20)
# my_push(10, size)  <-my_push 함수를 이용하든가
top += 1
stack[top] =20

def my_pop():
    global top
    if top == -1:
        print('Underflow')
        return 0
    else :
        top -= 1
        return stack[top+1]

print(my_pop())

if top > -1:   #pop()
    top -= 1
    print(stack[top+1])

    
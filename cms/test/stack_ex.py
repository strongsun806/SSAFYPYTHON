class Stack:
    def __init__(self, N):
        self.s = [None]*N
        self.top = -1
        self.length = N


    def push(self, value):
        if not self.is_full():
            self.top += 1
            self.s[self.top]=value
        else:
            print('스택이 가득찼습니다.')

    def pop(self):
        if not self.is_empty():
            value = self.s[self.top]
            self.top -=1
            return value
        else:
            print('스택이 비었습니다.')



    def is_full(self):
        if self.top ==self.length-1:
            return True
        return False

    def is_empty(self):
        if self.top == -1:
            return True
        return False

stack = Stack(5)

stack.push(3)
stack.push(5)
stack.push(4)
stack.push(2)
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)


print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
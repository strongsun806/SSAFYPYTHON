que = [0] * 10
front = rear = -1
rear += 1   # enqueue(1)
que[rear]=1
rear += 1   # enq2
que[rear]=2
rear += 1   # enq3
que[rear]=3

# front+=1
# print(que[front])
# front+=1
# print(que[front])
# front+=1
# print(que[front])

while front != rear:
    front +=1
    print(que[front])

q=[]    # 큐 생성
q.append(1)
q.append(2)
q.append(3)
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))

que= [0]*1000000
front= rear =-1
for i in range(1000000):
    q.append(i)
print(len(q))
for _ in range(1000000):
    q.pop(0)
print(len(q))
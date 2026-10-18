import sys
sys.stdin = open("input.txt", "r")

def is_empty():
    return front == rear

def is_full():
    return (rear + 1) % len(circle_queue) == front

def enqueue(item):
    global rear
    if is_full():
        print('Queue_Full')
    else:
        rear = (rear + 1) % len(circle_queue)
        circle_queue[rear] = item

def dequeue():
    global front
    if is_empty():
        print('Queue_Empty')
    else:
        front = (front + 1) % len(circle_queue)
        return circle_queue[front]


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    list_pizza_tmp = list(map(int, input().split()))  # 이거 길이는 M과 같음 ㅇㅇ
    list_pizza = []
    for i, j in enumerate(list_pizza_tmp):
        list_pizza.append([i + 1, j])  # i는 피자 인덱스이고, 실제 번호는 + 1 해야함.
                                       # j는 치즈 양

    circle_queue = [0] * (N + 1)
    front = rear = 0

    for i in range(N):
        enqueue(list_pizza[i])
        # 이러면 남은 피자들은 list_pizza[N:] 밖에서 기다리는 상태가 됨 ㅇㅇ
        # 암튼 이후에 pizza = dequeue()로 하나 꺼내서 확인하고,
        # 아직 안녹았으면 enqueue(pizza)로 다시 넣고,
        # 만약 녹았으면 빈자리가 생기므로 다음 피자를 enqueue(list_pizza[next_index])로 넣는 식임 ㅇㅇ

    next_index = N

    while not is_empty():
        pizza = dequeue()
        pizza[1] //= 2

        if pizza[1] == 0:  # 다 녹았다면
            # 다 녹아서 다시 enqueue()를 하지 않을 피자의 실제 번호를 따로 체크해두기
            # 
            answer = pizza[0]

            # 밖에 대기중인 피자가 있다면 다음 피자 투입
            if next_index < M:
                enqueue(list_pizza[next_index])
                next_index += 1

        # 아직 치즈가 덜 녹았다면 다시 화덕으로 빠꾸
        else:
            enqueue(pizza)

    print(f'#{test_case} {answer}')
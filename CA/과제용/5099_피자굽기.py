import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    # 피자의 초기 치즈 양과 피자 번호(1번부터 시작)
    cheese_list = list(map(int, input().split()))
    pizzas = [[i + 1, cheese_list[i]] for i in range(M)]
    
    # 화덕(크기 N)에 먼저 피자 넣기
    oven = deque()
    for _ in range(N):
        if pizzas:
            oven.append(pizzas.pop(0))
            
    # 화덕 돌리기
    while len(oven) > 1:
        pizza_num, cheese = oven.popleft()
        cheese = cheese // 2 # 한 바퀴 돌면 치즈가 반으로 줄어듦
        
        if cheese == 0:
            # 다 구워진 피자는 꺼내고, 남은 피자가 있으면 새로 넣기
            if pizzas:
                oven.append(pizzas.pop(0))
        else:
            # 아직 치즈가 남아있으면 다시 화덕에 넣기
            oven.append([pizza_num, cheese])
            
    # 마지막 남은 피자 번호
    last_pizza = oven[0][0]
    print(f"#{test_case} {last_pizza}")

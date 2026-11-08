import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

T = 10
for _ in range(T):
    test_case = int(input())
    queue = deque(map(int, input().split()))
    
    # 1싸이클에 1~5씩 순서대로 감소
    decrease = 1
    while True:
        num = queue.popleft() - decrease
        if num <= 0:
            queue.append(0)
            break
        queue.append(num)
        
        decrease += 1
        if decrease > 5:
            decrease = 1
            
    print(f"#{test_case}", *queue)

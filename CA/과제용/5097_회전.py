import sys
from collections import deque
# sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    num_list = deque(map(int, input().split()))
    
    # 맨 앞의 숫자를 빼서 맨 뒤로 보내기 M번 반복
    # (또는 num_list[M % N] 방식을 쓸 수도 있지만 큐의 흐름대로 직접 회전)
    rot_count = M % N
    for _ in range(rot_count):
        first = num_list.popleft()
        num_list.append(first)
        
    print(f"#{test_case} {num_list[0]}")

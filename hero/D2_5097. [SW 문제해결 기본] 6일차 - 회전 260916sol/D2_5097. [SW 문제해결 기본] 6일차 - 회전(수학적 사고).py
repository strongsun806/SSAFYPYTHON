import sys
sys.stdin = open("input.txt", "r")

# 수학적 사고 사용

# from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    list_1 = list(map(int, input().split()))

    # N개의 숫자를 N번 작업했다고 했을 때, 제자리로 돌아옴.
    # 따라서 M % N 을 해서 나머지를 찾고, 그 횟수만큼 작업을 하면 된다.
    # 여기에서 작업은 맨 앞의 숫자를 맨 뒤로 보내는 작업이라고 했으나,
    # 이는 왼쪽으로 회전하는 느낌으로 해석해도 된다.
    # 또한, 왼쪽으로 회전하는 것은 관찰자의 입장에서 포인터를 오른쪽으로 움직이는 것과 같다
    # 따라서 M % N 만큼 index 0에서 오른쪽으로 더해주면 된다.

    print(f'#{test_case} {list_1[M % N]}')
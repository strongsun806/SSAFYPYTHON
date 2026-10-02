import sys
sys.stdin = open("input.txt", "r")
from collections import deque

"""
문제 구상
8개의 숫자가 주어진다.
첫 번째 숫자를 꺼내서 1을 감소시킨 후 맨 뒤로 보낸다.
그다음 숫자는 2를 감소시킨 후 맨 뒤로 보내고
그다음은 3, 4, 5를 감소시킨다.
5까지 감소시킨 후 다시 1부터 반복한다.

로직 구상
1. q의 맨 앞 숫자를 꺼낸다.
2. 꺼낸 숫자에서 minus를 뺀다.
3. 결과가 0 이하인지 확인한다.
4. 만약 0 이하라면 q의 맨 뒤어 넣고 종료한다.
5. 만약 0보다 크다면 감소된 숫자를 q의 맨 뒤에 넣는다.
6. q 뒤에 넣을 때마다 minus를 1씩 증가시켜 1, 2, 3, 4, 5가 되도록 한다.
7. 만약 minus가 6이 된다면 1로 재할당해 다시 1부터 시작하도록 한다.
8. 반복한다.
9. 테스트케이스와 함께 q를 출력한다.
"""

def bfs(data):
    # 1. q의 맨 앞 숫자를 꺼낸다.
    q = deque(data)
    # 2. 꺼낸 숫자에서 minus를 뺀다.
    minus = 1

    # 3. 결과가 0이하가 될때까지 반복
    while True:
        num = q.popleft()
        num -= minus
        # 4. 만약 0 이하라면 0을 q의 맨 뒤어 넣고 종료한다.
        if num <= 0:
            q.append(0)
            break
        # 5. 만약 0보다 크다면 감소된 숫자를 q의 맨 뒤에 넣는다.
        q.append(num)
        # 6. q 뒤에 넣을 때마다 minus를 1씩 증가시켜 1, 2, 3, 4, 5가 되도록 한다.
        minus += 1
        # 7. 만약 minus가 6이 된다면 1로 재할당해 다시 1부터 시작하도록 한다.
        if minus == 6:
            minus = 1

    return q

# 9. 테스트케이스와 함께 q를 출력한다.
T = 10
for _ in range(1, T+1):
    test_case = int(input())
    data = list(map(int, input().split()))

    print(f'#{test_case}', *bfs(data))
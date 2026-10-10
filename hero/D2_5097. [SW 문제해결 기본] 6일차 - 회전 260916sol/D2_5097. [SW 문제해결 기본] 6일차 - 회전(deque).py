import sys
sys.stdin = open("input.txt", "r")

# deque 사용

from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    # 입력받은 숫자들을 deque로 만들기
    deque_1 = deque(map(int, input().split()))

    # 맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 반복
    for i in range(M):
        # rotate(-1)은 왼쪽으로 한 칸씩 회전
        # 즉 맨 앞의 값이 맨 뒤로 이동함
        # ex) [1, 2, 3] -> [2, 3, 1]
        deque_1.rotate(-1)

    print(deque_1)
    # M번 이동이 끝난 뒤 맨 앞에 있는 숫자 출력
    print(f'#{test_case} {deque_1[0]}')
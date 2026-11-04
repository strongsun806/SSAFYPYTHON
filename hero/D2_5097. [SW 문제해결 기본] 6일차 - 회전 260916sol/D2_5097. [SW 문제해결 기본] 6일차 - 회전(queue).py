import sys
sys.stdin = open("input.txt", "r")

# queue 사용

# from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    # N개의 숫자를 리스트로 입력받기
    list_1 = list(map(int, input().split()))

    # 맨 앞의 숫자를 빼서 맨 뒤로 보내는 작업을 M번 반복
    for i in range(M):
        # pop(0)으로 맨 앞 숫자를 빼고
        # append로 그 숫자를 다시 맨 뒤에 넣음
        # ex) [1, 2, 3] -> [2, 3, 1]
        list_1.append(list_1.pop(0))

    # M번 이동이 끝난 뒤 맨 앞에 있는 숫자 출력
    print(f'#{test_case} {list_1[0]}')
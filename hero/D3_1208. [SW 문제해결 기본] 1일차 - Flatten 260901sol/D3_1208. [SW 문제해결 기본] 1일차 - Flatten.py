import sys
sys.stdin = open("D3_1208. [SW 문제해결 기본] 1일차 - Flatten/input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    N = int(input()) # N은 주어진 덤프횟수
    list_num = list(map(int, input().split())) # 100개의 숫자열

    for i in range(N):
        list_num.sort(reverse=True)  # sort를 안에 넣은 이유: 숫자가 작아지거나 커지면서 최대 or 최솟값이 바뀔 수 있기 때문에 재정렬 필수
                                     # list_num을 내림차순으로 정렬 -> 숫자 관리하기 쉬움(0번이 최대, -1번이 최소).
                                     # 물론 오름차순으로 해도됨.
        list_num[0] = list_num[0] - 1    # 최댓값인 0번에는 -1을,
        list_num[-1] = list_num[-1] + 1  # 최솟값인 -1번에는 +1을 해주기 -> 덤프과정

    # 반복문 끝나고 정렬해줬을 때 인덱스0번과 -1번의 차이가 출력값
    list_num.sort(reverse=True)
    print(f'#{test_case} {list_num[0] - list_num[-1]}')
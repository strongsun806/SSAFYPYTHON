import sys
sys.stdin = open("input.txt", "r")

"""
로직 구상
1. 볼 수 있는 미래 일수 N을 입력받는다.
2. N일 동안의 매매가를 입력받는다.
3. 미래의 가격을 기준으로 판단하기 위해 마지막 날부터 거꾸로 확인한다.
4. 만약 지금 보는 가격이 가장 크다면 그 가격을 저장한다.
5. 지금 보는 가격이 가장 큰 가격보다 작다면 가장 비싼날에 판다고 생각해 두 가격의 차이를 이익에 더한다.
6. 모든 날을 확인할 때까지 반복한다.
7. 최종적으로 구한 이익을 테스트케이스와 함께 출력한다.
"""

T = int(input())
for test_case in range(1, T+1):
    # 1. 볼 수 있는 미래 일수 N을 입력받는다.
    N = int(input())
    # 2. N일 동안의 매매가를 입력받는다.
    sell_price = list(map(int, input().split()))

    # 4-1. 가장 큰 가격을 저장할 초기값 세팅
    max_price = 0
    # 5-1. 이익을 저장할 초기값 세팅
    income = 0
    # 6. 모든 날을 확인할 때까지 반복한다.
    # 3. 미래의 가격을 기준으로 판단하기 위해 마지막 날부터 거꾸로 확인한다.
    for i in range(N-1, -1, -1):
        # 4. 만약 지금 보는 가격이 가장 크다면 그 가격을 저장한다.
        if sell_price[i] > max_price:
            max_price = sell_price[i]
        # 5. 지금 보는 가격이 가장 큰 가격보다 작다면 가장 비싼날에 판다고 생각해 두 가격의 차이를 이익에 더한다.
        else:
            income += max_price - sell_price[i]
    # 7. 최종적으로 구한 이익을 테스트케이스와 함께 출력한다.
    print(f"#{test_case} {income}")
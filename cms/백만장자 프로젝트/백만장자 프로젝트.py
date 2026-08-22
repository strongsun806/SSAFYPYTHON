import sys
sys.stdin = open("input.txt", "r")

# 케이스 갯수 할당
T = int(input())
for test_case in range(1, T + 1):

    # 각 케이스의 길이
    length = int(input())
    # 각 케이스의 매매가 리스트
    history = list(map(int,input().split()))

    history_ex = history[::-1]
    timing = history_ex[0]
    profit = 0
    for price in history_ex :
        if timing <= price :
            timing = price
        else :
            profit += (timing-price)
    print(f"#{test_case} {profit}")

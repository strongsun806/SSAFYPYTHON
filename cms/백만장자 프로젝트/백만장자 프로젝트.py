import sys
sys.stdin = open("input.txt", "r")

# 케이스 갯수 할당
T = int(input())
for test_case in range(1, T + 1):

    # 각 케이스의 길이
    length = int(input())
    # 각 케이스의 매매가 리스트
    history = list(map(int,input().split()))
    # 리스트의 시계열을 뒤집은 history_ex리스트 할당
    history_ex = history[::-1]
    # 마지막 날의 매매가를 timing으로 할당
    timing = history_ex[0]
    # 이윤을 profit에 할당, 초기값 = 0
    profit = 0

    # 마지막날로 부터 앞으로 거슬러 올라감
    for price in history_ex :
        # 순회하면서 팔 타이밍 = 최고가로 할당함
        if timing <= price :
            timing = price
        # 최고가가 아니라면, 해당 타이밍에 물건을 사고, 최고가에 팔 때 생기는 이윤을 price에 추가
        else :
            profit += (timing-price)
    print(f"#{test_case} {profit}")

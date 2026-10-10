import sys
sys.stdin = open("input.txt", "r")

# n번 교환

# 1 2 3 4

# 1번 교환했을 때 모든 경우의 수
# -> 1 : 2 3 4
# -> 2 : 3 4
# -> 3 : 4
# i번 카드와 그 이후에 나오는 카드 바꿔보기


def shuffle(cards, count_1):
    global max_value

    num = int(''.join(cards))
                               
    if (count_1, num) in check:  # 이미 수행해본 경우의 수인지 확인
        return

    check.add((count_1, num))  # 교환 횟수랑 상태 같이 저장인데

    if count_1 >= N:
        
        if num > max_value:
            max_value = num
        # print(max_value)
        return

    for i in range(len(cards)):  # 교환하고자하는 앞쪽 카드
        for j in range(i + 1, len(cards)):  # 교환되려하는 뒤쪽 카드
            # i번과 j번을 교환 -> 여기까지하는게 1번 교환했을 때 모든 경우의 수 ㅇㅇ
            cards[i], cards[j] = cards[j], cards[i]
            # print(cards)
            shuffle(cards, count_1 + 1)
            # 원래대로 돌려놓기
            cards[i], cards[j] = cards[j], cards[i]


T = int(input())

for tc in range(1, T + 1):
    cards, N =input().split()
    cards = list(cards)
    N = int(N)
    max_value = 0

    # cards = ['1', '2', '3']

    # 중복교환을 막기 위해
    check = set()
    
    shuffle(cards, 0)

    print(f'#{tc} {max_value}')




##################### 잘 풀었지만 시간초과 ###########################
######## 다른 점: (교환 횟수 + 상태)까지 같다면 그걸 잘라내기 ##########

# def shuffle(cards, count_1):
#     global max_value

#     if count_1 >= N:
#         num = int(''.join(cards))
#         if num > max_value:
#             max_value = num
#         # print(max_value)
#         return

#     for i in range(len(cards)):  # 교환하고자하는 앞쪽 카드
#         for j in range(i + 1, len(cards)):  # 교환되려하는 뒤쪽 카드
#             # i번과 j번을 교환 -> 여기까지하는게 1번 교환했을 때 모든 경우의 수 ㅇㅇ
#             cards[i], cards[j] = cards[j], cards[i]
#             # print(cards)
#             shuffle(cards, count_1 + 1)
#             # 원래대로 돌려놓기
#             cards[i], cards[j] = cards[j], cards[i]


# T = int(input())

# for tc in range(1, T + 1):
#     cards, N =input().split()
#     cards = list(cards)
#     N = int(N)
#     max_value = 0

#     # cards = ['1', '2', '3']

    
#     shuffle(cards, 0)

#     print(f'#{tc} {max_value}')
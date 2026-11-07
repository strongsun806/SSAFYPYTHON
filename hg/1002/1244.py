# 카드를 한 번 교환하는 경우의 수는
# i번 카드와 그 이후에 나오는 카드 바꿔보기
# for i in range(N):
#     for j in range(i+1,N):
#         i번과 j번을 교환
def suffle(cards, cnt):
    global max_v
    num = int(''.join(cards))
    if (cnt, num) in check:  # 이미 수행해본 경우의 수인지 확인
        return

    check.add((cnt, num))  # 교환 횟수랑 상태랑 같이 저장
    if cnt == N:
        # print(cards)
        if num > max_v:
            max_v = num
        return
    # 한 번 교환하는 모든 경우의 수
    for i in range(len(cards)):
        for j in range(i + 1, len(cards)):
            # 카드교환
            cards[i], cards[j] = cards[j], cards[i]
            # print(cards)
            # cnt + 1 : 카드 교환횟수 증가
            suffle(cards, cnt + 1)
            # 원래모양으로 바꾸기,
            cards[i], cards[j] = cards[j], cards[i]


T = int(input())
for tc in range(1, T + 1):
    cards, N = input().split()
    cards = list(cards)
    # print(cards, N)
    N = int(N)
    max_v = 0
    # 중복 교환을 막기위해서 set()
    check = set()
    suffle(cards, 0)
    print(f'#{tc} {max_v}')
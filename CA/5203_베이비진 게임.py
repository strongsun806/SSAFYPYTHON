# sys.stdin = open("input.txt", "r")

def is_babygin(cnt):
    # triplet 검사
    for num in range(10):
        if cnt[num] >= 3:
            return True
            
    # run 검사
    for num in range(8):
        if cnt[num] >= 1 and cnt[num + 1] >= 1 and cnt[num + 2] >= 1:
            return True
            
    return False

T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))
    
    p1_cnt = [0] * 10
    p2_cnt = [0] * 10
    winner = 0
    
    for i in range(12):
        card = cards[i]
        
        # 짝수 턴은 1번 플레이어, 홀수 턴은 2번 플레이어
        if i % 2 == 0:
            p1_cnt[card] += 1
            if is_babygin(p1_cnt):
                winner = 1
                break
        else:
            p2_cnt[card] += 1
            if is_babygin(p2_cnt):
                winner = 2
                break
                
    print(f"#{tc} {winner}")

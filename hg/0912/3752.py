T = int(input())

for tc in range(1, T + 1):
    N = int(input().strip())
    
    # 점수 데이터가 여러 줄에 나뉘어 들어오는 경우 대비
    scores = []
    while len(scores) < N:
        scores.extend(map(int, input().split()))
    
    # 0점을 의미하는 0번째 비트 활성화를 해용
    mask = 1
    for s in scores:
        mask |= (mask << s)
    
    # 켜진 비트(가능한 점수)의 개수를 카운트 해보까요
    ans = bin(mask).count('1')
    
    print(f"#{tc} {ans}")
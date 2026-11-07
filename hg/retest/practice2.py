T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    
    pair_diffs = []
    for i in range(N // 2):
        # 두 수의 차이 구하기 (큰 수 - 작은 수 = 절댓값)
        diff = nums[i] - nums[N - 1 - i]
        if diff < 0:
            diff = -diff
        pair_diffs.append(diff)
        
    ans = 1
    # 이번에는 '계속 감소' 해야 하므로, 앞이 뒤보다 작거나 같으면 탈락
    for i in range(len(pair_diffs) - 1):
        if pair_diffs[i] <= pair_diffs[i+1]:
            ans = 0
            break
    
    print(f"#{tc} {ans}")
    
    
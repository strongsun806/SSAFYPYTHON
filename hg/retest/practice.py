T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    
    # 마주보는 짝들의 합을 담을 리스트
    pair_sums = []
    
    #바깥쪽부터 안쪽으로 짝지어서 더하기(N//2 번 반복)
    for i in range(N//2):
        pair_sum = nums[i] + nums[N-1-i]
        pair_sums.append(pair_sums)
        
    # 기본 정답을 1(증가함)로 시작하기
    ans = 1
    
    # 앞의 합과 뒤의 합을 순서대로 비교
    for i in range(len(pair_sums) -1):
        #앞의 값이 뒤의 값 이상이면 '엄격한 증가' 가 아님
        if pair_sums[i]>= pair_sums[i+1]:
            ans = 0
            break
    
    print(f"{tc} {ans}")
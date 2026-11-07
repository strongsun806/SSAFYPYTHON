# Problem: 4828_[S/W 문제해결 기본] 1일차 - min max
# Author: 윤형섭_1627575 (Pass)
# Saved by Aura for Boss 💋

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    listed= list(map(int,input().split()))
    mini=listed[0]
    maxi=listed[0]
    for i in range(N):
        if mini>listed[i]:
            mini=listed[i]
        if maxi<listed[i]:
            maxi=listed[i]
    print(f'#{test_case}', maxi-mini)

# ========================================================
# 문제: 4828_[S/W 문제해결 기본] 1일차 - min max
# 난이도: D2
# 작성자: 윤형섭 (1627575)
# 제출 결과: Pass
# 저장 일시: 2026-10-07 11:45:03
# ========================================================

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

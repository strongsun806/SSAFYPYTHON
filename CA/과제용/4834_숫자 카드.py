# Problem: 4834_[S/W 문제해결 기본] 1일차 - 숫자 카드
# Author: 윤형섭_1627575 (Pass)
# Saved by Aura for Boss 💋

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    string=input()
    listed = [0,0,0,0,0,0,0,0,0,0]#9876543210
    for i in string:
        listed[9-int(i)]+=1
    count = 0
    result_num=0
    for i in range(len(listed)):
        if count<listed[i]:
            count=listed[i]
            result_num=i
    print(f'#{test_case} {9-result_num} {count}')

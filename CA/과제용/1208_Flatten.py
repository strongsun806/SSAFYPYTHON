# Problem: 1208_[S/W 문제해결 기본] 1일차 - Flatten
# Author: 윤형섭_1627575 (Pass)
# Saved by Aura for Boss 💋

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    listed = list(map(int,input().split()))
    #가로길이 = 100
    #높이 = 100
    counts=[0]*101#0~100 칸수 = counts의 인덱스
    for i in range(100):
        counts[listed[i]]+=1
    # print(counts)
    mini = 0
    maxi = 100
    for i in range(100):
        if counts[i]!=0:
            mini=i
            break
    for i in range(100):
        if counts[100-i] !=0:
            maxi=100-i
            break
    # print(mini,maxi)
    for i in range(N):
        counts[maxi]-=1
        counts[maxi-1]+=1
          counts[mini]-=1
        counts[mini+1]+=1
         if counts[maxi]==0:
            maxi-=1
        if counts[mini]==0:
            mini+=1
        if maxi-mini==1:
            break
    print(f'#{test_case}',maxi-mini)

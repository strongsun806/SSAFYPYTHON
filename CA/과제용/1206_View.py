# Problem: 1206_[S/W 문제해결 기본] 1일차 - View
# Author: 윤형섭_1627575 (Pass)
# Saved by Aura for Boss 💋

T=10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr=list(map(int,input().split()))
     count=0
    #우측조망
    left_po = []
    right_po = []
    for i in range(N):
        left_po+=[0]
        right_po+=[0]
     for i in range(2,N-2):#0123456789
        if arr[i]>arr[i+1] and arr[i]>arr[i+2]: # 2,3,4비교~ n-3 n-2 n-1 비교
            if arr[i+1]>=arr[i+2]:
                left_po[i]=arr[i]-arr[i+1]
            else:
                left_po[i]=arr[i]-arr[i+2]
        if arr[i]>arr[i-1] and arr[i]>arr[i-2]:#
            if arr[i-1]>=arr[i-2]:
                right_po[i]=arr[i]-arr[i-1]
            else:
                right_po[i]= arr[i]-arr[i-2]
    for i in range(2,N-2):
        if left_po[i]>=1 and right_po[i]>=1:
            if left_po[i]>right_po[i]:
                count+=right_po[i]
            else:
                count+=left_po[i]
    print(f'#{test_case}',count)

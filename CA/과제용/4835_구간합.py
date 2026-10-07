# Problem: 4835_[S/W 문제해결 기본] 1일차 - 구간합
# Author: 윤형섭_1627575 (Pass)
# Saved by Aura for Boss 💋

#import sys
#sys.stdin = open("input.txt", "r")
 T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = list(map(int,input().split()))# 10 3
    listed = list(map(int,input().split()))
    first=0
    for i in range(M):#012번 합침 M이 3일때
        first+=listed[i]#6
     max=first
    min=first
    for i in range(M,N):#1 2 3 4 5 6 7 8 9 10
        first+=listed[i]-listed[i-M]
        if first>max:
            max=first
        if first<min:
            min=first
    print(f"#{test_case}",max-min)

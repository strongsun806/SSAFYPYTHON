# Problem: 6485_삼성시의 버스 노선
# Author: 윤형섭_1627575 (Pass)
# Saved by Aura for Boss 💋

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    listed =[0]
    for _ in range(N):
        listed.append(list(map(int,input().split())))#리스티드 안에,listed[i]=[ai,bi]집어 넣음
    P= int(input())
    c_list=[]
    for _ in range(P):
        c_list.append(int(input()))
    # print(listed)
    # print(c_list)
    result=[]
    for i in range(P):
        count=0
        for j in range(1,N+1):
            if (listed[j][0] <= c_list[i]) and c_list[i] <= listed[j][1]:
               count+=1
        result.append(count)
    print(f'#{test_case}', *result)

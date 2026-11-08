# ========================================================
# 문제: 1859_백만 장자 프로젝트
# 난이도: D2
# 작성자: 윤형섭 (1627575)
# 제출 결과: Pass
# 저장 일시: 2026-10-07 11:46:55
# ========================================================

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    count = 0
    pay = 0
    def buy(n):
        global count, pay
        count+=1
        pay -= n
        pass
    def sell(n):
        global count, pay
        pay += count*n
        count=0
        pass
    N = int(input())
    all_list=list(map(int,input().split()))
    iter = range(len(all_list))
    maximum=max(all_list)#9
    max_list=[]
    for i in iter :#0 1 2 3...16
                 if all_list[i]==maximum:
            max_list.append(i)
            if (i+1)!=N:
                maximum=max(all_list[i+1::])
    # print(max_list)
    for i in iter:
        if i in max_list:
            sell(all_list[i])
        else:
            buy(all_list[i])
    print(f'#{test_case} {pay}')

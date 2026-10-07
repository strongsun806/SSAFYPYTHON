# ========================================================
# 문제: 13065_5189. [파이썬 S/W 문제해결 구현] 2일차 - 전자카트
# 난이도: D3
# 작성자: 윤형섭 (1627575)
# 제출 결과: Pass
# 저장 일시: 2026-10-07 11:28:19
# ========================================================

from math import inf
# sys.stdin = open("input.txt", "r")
 t = int(input())
#순열 만들기
#[2,3,4....,n]
   # path = [""] * 3 # 카드 묶음의 개수 (level)
# used = [0]*4 # 선택할 수 있는 카드 종류 개수(branch)
  # def abc(level):
#     if level == 3:
#         print(*path)
#         return
 #     for i in range(4):
#         if used[i] == 1: continue
#         used[i] = 1
#         path[level] = card[i]
#         abc(level+1)
#         path[level] = ""
#         used[i] = 0
 # abc(0)
 def 순열(n,level):
    global path
    global used
    global 수운열
    who=list(range(2,n+1)) #2부터 n까지
    if level == n-2+1:
        수운열+=[path.copy()]
        return
    for i in range(n-2+1):
        if used[i] == 1: continue
        used[i] = 1
        path[level] = who[i]
        순열(n,level+1)
        # path[level] = ""
        used[i] = 0
  for tc in range(1,t+1):
    n=int(input())
    path=[None]*(n-1)
    used = [0]*(n-2+1)
    수운열=[]
    # [[0, 0, 0, 0],
    # [0, 0, 18, 34],
    # [0, 48, 0, 55],
    # [0, 18, 7, 0]]
    listed = [[0]*(n+1)]
    listed +=[([0]+ list(map(int,input().split()))) for _ in range(n)]
    순열(n,0)
    # print(수운열)
    #pprint (listed)
    #listed[출발][도착]
    result=float(inf)
    for i in range(len(수운열)):
        count=0
        count+=listed[1][수운열[i][0]]
        for j in range(n-2):
            count+=listed[수운열[i][j]][수운열[i][j+1]]
         count+=listed[수운열[i][n-2]][1]
        if count<result:
            result=count
    print(f'#{tc}',result)
